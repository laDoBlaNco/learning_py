# my_spdump.py

import sqlite3

conn = sqlite3.connect("my_spider.sqlite")
cur = conn.cursor()

cur.execute("""select count(from_id) as inbound,old_rank,new_rank,id,url
            from pages join links on pages.id=links.to_id
            where html is not null
            group by id order by inbound desc""")

count = 0
for row in cur:
    if count < 50:
        print(row)
    count += 1
print(count, "rows.")
cur.close()
