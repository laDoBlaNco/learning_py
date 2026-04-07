# tracks.py

import sqlite3

conn = sqlite3.connect("trackdb.sqlite")
cur = conn.cursor()

# make some fresh tables using .executescript() (this is new 🤔)
cur.executescript("""
                  drop table if exists artist;
                  drop table if exists album;
                  drop table if exists track;

                  create table Artist(
                  id integer primary key,
                  name text unique
                  );

                  create table Album(
                  id integer primary key,
                  artist_id integer,
                  title text unique
                  );

                  create table track(
                  id integer primary key,
                  title text unique,
                  album_id integer,
                  len integer,
                  rating integer,
                  count integer
                  );               
                  """)
handle = open("tracks.csv")

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                           1   2            3   4   5

for line in handle:
    line = line.strip()
    pieces = line.split(",")
    if len(pieces) < 6:
        continue
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]

    print(name, artist, album, count, rating, length)

    cur.execute(
        """insert or ignore into artist(name)
                values(?)""",
        (artist,),
    )
    cur.execute("select id from artist where name = ?", (artist,))
    # on entering we don't know what the artist_id will be so we need
    # to get it first and put it in a var.
    artist_id = cur.fetchone()[0]

    cur.execute(
        """insert or ignore into album (title,artist_id)
                values(?,?)""",
        (album, artist_id),
    )
    cur.execute("select id from album where title = ?", (album,))
    album_id = cur.fetchone()[0]

    cur.execute(
        """insert or replace into track (title,album_id,len,rating,count)
                values(?,?,?,?,?)""",
        (name, album_id, length, rating, count),
    )

    conn.commit()

