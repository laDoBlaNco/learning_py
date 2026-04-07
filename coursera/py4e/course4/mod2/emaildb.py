# emaildb.py

import sqlite3

conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute(""" 
drop table if exists Counts """)

cur.execute("""
create table Counts (email TEXT, count INTEGER)
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
    cur.execute("select count from counts where email = ? ", (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute(
            """insert into counts (email,count)
                    values(?,1)""",
            (email,),
        )
    else:
        cur.execute("update counts set count = count + 1 where email = ?", (email,))
        # I remember this from my php class. The '?' is a placeholder so we don't
        # allow sql injection. (email,) is a python typle, which is why its (email,)
    conn.commit()

sqlstr = 'select email,count from counts order by count desc limit 10'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

