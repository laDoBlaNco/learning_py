# my_gbasic.py

import sqlite3

howmany = int(input("How many to dump? "))

conn = sqlite3.connect('my_index.sqlite')
cur = conn.cursor()

cur.execute('select id,sender from senders')
senders = {}
for message_row in cur:
    senders[message_row[0]] = message_row[1]

cur.execute('select id,subject from subjects')
subjects = {}
for message_row in cur:
    subjects[message_row[0]] = message_row[1]

cur.execute('select id,guid,sender_id,subject_id,sent_at from messages')
messages = {}
for message_row in cur:
    messages[message_row[0]] = message_row[1],message_row[2],message_row[3],message_row[4]

print(f"Loaded messages={len(messages)}, subjects={len(subjects)}, senders={len(senders)}")

sendcounts = {}
sendorgs = {}
for message_id,message in messages.items():
    sender=message[1]
    sendcounts[sender]=sendcounts.get(sender,0)+1
    pieces = senders[sender].split('@')
    if len(pieces)!=2:
        continue
    dns = pieces[1]
    sendorgs[dns]=sendorgs.get(dns,0)+1

print()
print(f"Top {howmany} Email list participants")

x = sorted(sendcounts,key=sendcounts.get,reverse=True)
for k in x[:howmany]:
    print(senders[k],sendcounts[k])
    if sendcounts[k] < 10:
        break

print()
print(f"Top {howmany} Email list organizations")

x = sorted(sendorgs,key=sendorgs.get,reverse=True)
for k in x[:howmany]:
    print(k,sendorgs[k])
    if sendorgs[k]<10:
        break
    