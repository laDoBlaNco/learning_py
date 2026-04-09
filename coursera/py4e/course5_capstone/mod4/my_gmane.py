# my_gmane.py

import sqlite3
import time
import ssl
import urllib.request
import urllib.parse
import urllib.error
import re
from datetime import datetime


# not all system have this, so we conditionally create a parser
try:
    import dateutil.parser as parser  # type: ignore
except Exception:
    ...


def parseemaildate(md):
    # see if we have dateutil
    try:
        pdate = parser.parse(md)
        test_at = pdate.isoformat()
        return test_at
    except:  # noqa: E722
        ...

    # non-dateutil version - we try our best
    pieces = md.split()
    notz = " ".join(pieces[:4]).strip()

    # try a bunch of format variations - strptime()
    dnotz = None
    for form in [
        "%d %b %Y %H:%M:%s",
        "%d %b %Y %H:%M:%S",
        "%d %b %Y %H:%M",
        "%d %b %Y %H:%M",
        "%d %b %y %H:%M:%S",
        "%d %b %y %H:%M:%S",
        "%d %b %y %H:%M",
        "%d %b %y %H:%M",
    ]:
        try:
            dnotz = datetime.strptime(notz, form)
            break
        except Exception:
            continue

    if dnotz is None:
        # print('Bad Date:',md)
        return None

    iso = dnotz.isoformat()

    tz = "+0000"
    try:
        tz = pieces[4]
        ival = int(tz)  # so we only get numeric timezones  # noqa: F841
        if tz == "-0000":
            tz = "+0000"
        tzh = tz[:3]
        tzm = tz[3:]
        tz = f"{tzh}:{tzm}"
    except Exception:
        ...

    return iso + tz


# ignore ssl cert trick
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("my_content.sqlite")
cur = conn.cursor()

baseurl = "https://mbox.dr-chuck.net/sakai.devel/"

cur.execute("""create table if not exists Messages
            (id integer unique,email text,sent_at text,
            subject text,headers text,body text)""")

# pick up where we left off
start = None
cur.execute("select max(id) from Messages")
try:
    row = cur.fetchone()
    if row is None:
        start = 0
    else:
        start = row[0]
except Exception:
    start = 0

if start is None:
    start = 0

many = 0
count = 0
fail = 0
while True:
    if many < 1:
        conn.commit()
        sval = input("How many messages: ")
        if len(sval) < 1:
            break
        many = int(sval)

    start = start + 1
    cur.execute("select id from messages where id=?", (start,))
    try:
        row = cur.fetchone()
        if row is not None:
            continue
    except Exception:
        row = None

    many -= 1
    url = f"{baseurl}{start}/{start + 1}"

    text = "None"
    try:
        # open with a timeout of 30 seconds
        document = urllib.request.urlopen(url, None, 30, context=ctx)
        text = document.read().decode()
        if document.getcode() != 200:
            print(f"Error code = {document.getcode()} {url}")
            break
    except KeyboardInterrupt:
        print()
        print("Program interrupted by user...")
        break
    except Exception as e:
        print(f"Unable to retrieve or parse page {url}")
        print(f"Error: {e}")
        fail += 1
        if fail > 5:
            break
        continue

    print(f"{url}: {len(text)}")
    count += 1

    if not text.startswith("From "):
        print(text)
        print("Did not find From ")
        fail += 1
        if fail > 5:
            break
        continue

    pos = text.find("\n\n")
    if pos > 0:
        hdr = text[:pos]
        body = text[pos + 2 :]
    else:
        print(text)
        print("Could not find break between headers and body")
        fail += 1
        if fail > 5:
            break
        continue

    email = None
    x = re.findall(r"\nFrom: .* <(\S+@\S+)>\n", hdr)
    if len(x) == 1:
        email = x[0]
        email = email.strip().lower()
        email = email.replace("<", "")
    else:
        x = re.findall(r"\nFrom: (\S+@\S+)\n", hdr)
        if len(x) == 1:
            email = x[0]
            email = email.strip().lower()
            email = email.replace("<", "")

    date = None
    y = re.findall(r"\nDate: .*, (.*)\n", hdr)
    if len(y) == 1:
        tdate = y[0]
        tdate = tdate[:26]
        try:
            sent_at = parseemaildate(tdate)
        except Exception:
            print(text)
            print(f"Parse fail: {tdate}")
            fail += 1
            if fail > 5:
                break
            continue
    subject = None
    z = re.findall(r"\nSubject: (.*)\n", hdr)
    if len(z) == 1:
        subject = z[0].strip().lower()

    # reset the fail counter
    fail = 0

    print(f"    {start}: {email} {sent_at} {subject}")
    cur.execute(
        """insert or ignore into messages(id,email,sent_at,subject,headers,body)
                values(?,?,?,?,?,?)""",
        (start, email, sent_at, subject, hdr, body),
    )
    if count % 50 == 0:
        conn.commit()
    if count % 100 == 0:
        time.sleep(1)
conn.commit()
cur.close()
