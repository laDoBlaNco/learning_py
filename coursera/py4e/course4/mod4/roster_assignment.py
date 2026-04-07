# roster_assignment.py

import json
import sqlite3

conn = sqlite3.connect("rosterdb_assignment.sqlite")
cur = conn.cursor()

# do some setup as always
cur.executescript("""
                  drop table if exists user;
                  drop table if exists member;
                  drop table if exists course;

                  create table User(
                  id integer not null primary key autoincrement unique,
                  name text unique
                  );

                  create table Course(
                  id integer not null primary key autoincrement unique,
                  title text unique
                  );

                  create table Member(
                  user_id integer,
                  course_id integer,
                  role integer,
                  primary key (user_id,course_id)
                  );                  

""")

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "roster_data.json"

# Example of the data format
# [
#     ['Charley','si110',1],
#     ['Mea','si110',0],
# ]

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title,role))

    cur.execute(
        """insert or ignore into user (name)
                values (?)""",
        (name,),
    )
    cur.execute("select id from user where name=?", (name,))
    user_id = cur.fetchone()[0]

    cur.execute(
        """insert or ignore into course(title)
                values(?)""",
        (title,),
    )
    cur.execute("select id from course where title=?", (title,))
    course_id = cur.fetchone()[0]

    cur.execute(
        "insert or replace into member(user_id,course_id,role) values(?,?,?)",
        (user_id, course_id,role),
    )

    conn.commit()
