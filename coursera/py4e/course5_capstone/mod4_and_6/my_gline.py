# my_gline.py
import sqlite3

conn = sqlite3.connect('my_index.sqlite')
cur = conn.cursor()

cur.execute('select id,sender from senders')
senders = {}
for msg_row in cur:
    senders[msg_row[0]] = msg_row[1]

cur.execute('select id,guid,sender_id,subject_id,sent_at from messages')
messages = {}
for msg_row in cur:
    messages[msg_row[0]] = msg_row[1],msg_row[2],msg_row[3],msg_row[4]

print(f"Loaded messages={len(messages)}, senders={len(senders)}")

sendorgs={}
for message_id,message in messages.items():
    sender=message[1]
    pieces = senders[sender].split('@')
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    sendorgs[dns] = sendorgs.get(dns,0)+1

# pick the top schools
orgs = sorted(sendorgs,key=sendorgs.get,reverse=True)
orgs = orgs[:10]
print("Top 10 Organizations")
print(orgs)

counts = {}
months = []

for message_id,message in messages.items():
    sender = message[1]
    pieces = senders[sender].split('@')
    if len(pieces) != 2:
        continue
    dns = pieces[1]
    if dns not in orgs:
        continue
    month = message[3][:7]
    if month not in months:
        months.append(month)
    key = month,dns
    counts[key] = counts.get(key,0)+1

months.sort()
# print(counts)

fhand = open('my_gline.js','w')
fhand.write("gline = [ ['Year'")
for org in orgs:
    fhand.write(f",'{org}'")
fhand.write("]")

for month in months:
    fhand.write(f",\n['{month}'")
    for org in orgs:
        key = month,org
        val = counts.get(key,0)
        fhand.write(f",{str(val)}")
    fhand.write("]")

fhand.write("\n];\n")

print("Output written to my_gline.js")
print("Open my_gline.htm to visualize the data")

