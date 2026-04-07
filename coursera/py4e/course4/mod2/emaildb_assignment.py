# emaildb.py

import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute(""" 
drop table if exists Counts """)

cur.execute("""
create table Counts (org TEXT, count INTEGER)
""")

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox.txt"
fh = open(fname)

for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email[email.find('@')+1:]
    cur.execute("select count from counts where org = ? ", (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            """insert into counts (org,count)
                    values(?,1)""",
            (org,),
        )
    else:
        cur.execute("update counts set count = count + 1 where org = ?", (org,))
        # I remember this from my php for everyone class. The '?' is a placeholder so we don't
        # allow sql injection. (org,) is a python typle, which is why its (org,)
conn.commit()

sqlstr = "select org,count from counts order by count desc limit 10"

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
