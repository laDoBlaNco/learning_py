# my_spreset.py
import sqlite3

conn = sqlite3.connect('my_spider.sqlite')
cur = conn.cursor()

cur.execute('update pages set new_rank=1.0,old_rank=0.0')
conn.commit()

cur.close()

print('All pages set to a rank of 1.0')


