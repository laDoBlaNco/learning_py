# my_gmodel.py
import sqlite3
import re
import zlib
import dateutil.parser as parser  # type: ignore


dnsmapping = {}
mapping = {}


def fixsender(sender, allsenders=None):
    global dnsmapping
    global mapping
    if sender is None:
        return None
    sender = sender.strip().lower()
    sender = sender.replace("<", "").replace(">", "")

    # check if we have a hacked gmane.org from address
    if allsenders is not None and sender.endswith("gmane.org"):
        pieces = sender.split("-")
        realsender = None
        for s in allsenders:
            if s.startswith(pieces[0]):
                realsender = sender
                sender = s
                # print(realsender,sender)
                break
        if realsender is None:
            for s in mapping:
                if s.startswith(pieces[0]):
                    realsender = sender
                    sender = mapping[s]
                    # print(realsender,sender)
                    break
        if realsender is None:
            sender = pieces[0]

    mpieces = sender.split("@")
    if len(mpieces) != 2:
        return sender
    dns = mpieces[1]
    x = dns  # noqa: F841
    pieces = dns.split(".")
    if (
        dns.endswith(".edu")
        or dns.endswith(".com")
        or dns.endswith(".org")
        or dns.endswith(".net")
    ):
        dns = ".".join(pieces[-2:])
    else:
        dns = ".".join(pieces[-3:])
    # if dns != x: print(x,dns)
    # if dsn != dsnmapping.get(dns,dns): print(dns,dnsmapping.get(dns,dns))
    dns = dnsmapping.get(dns, dns)
    return f"{mpieces[0]}@{dns}"


def parsemaildate(md):
    # see if we have dateutil and it works
    try:
        pdate = parser.parse(md)
        test_at = pdate.isoformat()
        return test_at
    except Exception:
        ...


# parse otu the info...
def parseheader(hdr, allsenders=None):
    if hdr is None or len(hdr) < 1:
        return None
    sender = None
    x = re.findall(r"\nFrom: .* <(\S+@\S+)>\n", hdr)
    if len(x) >= 1:
        sender = x[0]
    else:
        x = re.findall(r"\nFrom: (\S+@\S+)\n", hdr)
        if len(x) >= 1:
            sender = x[0]

    # normalize the domain name of Email addresses
    sender = fixsender(sender, allsenders)

    date = None  # noqa: F841
    y = re.findall(r"\nDate: .*, (.*)\n", hdr)
    sent_at = None
    if len(y) >= 1:
        tdate = y[0]
        tdate = tdate[:26]
        try:
            sent_at = parsemaildate(tdate)
        except Exception as e:  # noqa: F841
            # print('Date ignored ',tdate,e)
            return None

    subject = None
    z = re.findall(r"\nSubject: (.*)\n", hdr)
    if len(z) >= 1:
        subject = z[0].strip().lower()

    guid = None
    z = re.findall(r"\nMessage-ID: (.*)\n", hdr)
    if len(z) >= 1:
        guid = z[0].strip().lower()

    if sender is None or sent_at is None or subject is None or guid is None:
        return None
    return (guid, sender, subject, sent_at)


conn = sqlite3.connect("my_index.sqlite")
cur = conn.cursor()

cur.execute("drop table if exists Messages")
cur.execute("drop table if exists Senders")
cur.execute("drop table if exists Subjects")
cur.execute("drop table if exists Replies")

cur.execute("""create table if not exists Messages
            (id integer primary key,guid text unique,sent_at integer,
            sender_id integer,subject_id integer,headers blob, body blob)""")
cur.execute("""create table if not exists Senders
            (id integer primary key,sender text unique)""")
cur.execute("""create table if not exists Subjects
            (id integer primary key, subject text unique)""")
cur.execute("""create table if not exists Replies
            (from_id integer,to_id integer)""")

conn_1 = sqlite3.connect("my_mapping.sqlite")
cur_1 = conn_1.cursor()

cur_1.execute("select old,new from DNSMapping")
for message_row in cur_1:
    dnsmapping[message_row[0].strip().lower()] = message_row[1].strip().lower()

mapping = {}
cur_1.execute("select old,new from Mapping")
for message_row in cur_1:
    old = fixsender(message_row[0])
    new = fixsender(message_row[1])
    mapping[old] = fixsender(new)

# done with mapping.sqlite
conn_1.close()

# open the main content (Read only) a trick to run both at the same
# time on the same db as the spider might take much longer to run
conn_1 = sqlite3.connect("file:my_content.sqlite?mode=ro", uri=True)
cur_1 = conn_1.cursor()

allsenders = []
cur_1.execute("select email from Messages")
for message_row in cur_1:
    sender = fixsender(message_row[0])
    if sender is None:
        continue
    if "gmane.org" in sender:
        continue
    if sender in allsenders:
        continue
    allsenders.append(sender)

print(
    f"Loaded allsenders {len(allsenders)} and mapping {len(mapping)} and dns mapping {len(dnsmapping)}"
)

cur_1.execute('select headers,body,sent_at from messages order by sent_at')

senders = {}
subjects = {}
guids = {}

count = 0

for message_row in cur_1:
    hdr = message_row[0]
    parsed = parseheader(hdr,allsenders)
    if parsed is None:
        continue
    guid,sender,subject,sent_at = parsed

    # apply the sender mapping
    sender = mapping.get(sender,sender)

    count+=1
    if count % 250==1:
        print(count,sent_at,sender)

    # print(guid,sender,subject,sent_at)

    if 'gmane.org' in sender:
        print(f"Error in sender === {sender}")

    sender_id = senders.get(sender,None)
    subject_id = subjects.get(subject,None)
    guid_id = guids.get(guid,None)

    if sender_id is None:
        cur.execute('insert or ignore into senders(sender) values(?)',(sender,))
        conn.commit()
        cur.execute('select id from senders where sender=? limit 1',(sender,))
        try:
            row = cur.fetchone()
            sender_id = row[0]
            senders[sender] = sender_id
        except Exception:
            print(f"Could not retrieve sender id {sender}")
            break
    
    if subject_id is None:
        cur.execute("insert or ignore into subjects (subject) values (?)",(subject,))
        conn.commit()
        cur.execute("select id from subjects where subject=? limit 1",(subject,))
        try:
            row = cur.fetchone()
            subject_id = row[0]
            subjects[subject] = subject_id
        except Exception:
            print(f"Could not retrieve subject id {subject}")
            break

    # print(sender_id,subject_id)
    cur.execute('insert or ignore into messages (guid,sender_id,subject_id,sent_at,headers,body) values(?,?,?,datetime(?),?,?)',
                (guid,sender_id,subject_id,sent_at,zlib.compress(message_row[0].encode()),zlib.compress(message_row[1].encode())))
    
    conn.commit()
    cur.execute('select id from messages where guid=? limit 1',(guid,))
    try:
        row=cur.fetchone()
        message_id=row[0]
        guids[guid]=message_id
    except Exception:
        print(f"Could not retrieve guid id {guid}")
        break

cur.close()
cur_1.close()
