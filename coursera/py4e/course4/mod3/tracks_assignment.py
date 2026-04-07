# tracks.py

import sqlite3

conn = sqlite3.connect("trackdb_assignment.sqlite")
cur = conn.cursor()

# make some fresh tables using .executescript() (this is a new one 🤔)
cur.executescript("""
                  drop table if exists artist;
                  drop table if exists genre;
                  drop table if exists album;
                  drop table if exists track;

                  create table Artist(
                  id integer not null primary key autoincrement unique,
                  name text unique
                  );

                  create table Genre(
                  id integer not null primary key autoincrement unique,
                  name text unique
                  );

                  create table Album(
                  id integer not null primary key autoincrement unique,
                  artist_id integer,
                  title text unique
                  );

                  create table Track(
                  id integer not null primary key autoincrement unique,
                  title text unique,
                  album_id integer,
                  genre_id integer,
                  len integer,
                  rating integer,
                  count integer
                  );               
                  """)
handle = open("tracks.csv")

# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103,Rock
#   0                           1   2            3   4   5      6

for line in handle:
    line = line.strip()
    pieces = line.split(",")
    if len(pieces) < 7:
        continue
    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genre = pieces[6]

    print(name, artist, album, count, rating, length, genre)

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
        """insert or ignore into genre(name)
                values (?)""",
        (genre,),
    )
    cur.execute("select id from genre where name = ?", (genre,))
    genre_id = cur.fetchone()[0]

    cur.execute(
        """insert or ignore into album (title,artist_id)
                values(?,?)""",
        (album, artist_id),
    )
    cur.execute("select id from album where title = ?", (album,))
    album_id = cur.fetchone()[0]

    cur.execute(
        """insert or replace into track (title,album_id,genre_id,len,rating,count)
                values(?,?,?,?,?,?)""",
        (name, album_id, genre_id, length, rating, count),
    )

    conn.commit()
