# my_sprank.py

import sqlite3

conn = sqlite3.connect("my_spider.sqlite")
cur = conn.cursor()

# first we find the ids that send out page rank - we are only interested in
# pages in the SCC that have in and out links
cur.execute("select distinct from_id from links")
from_ids = []
for row in cur:
    # print(row)
    from_ids.append(row[0])
    # NOTE: seeing from my debug print statement that each row in cur is actually
    # a python tuple. That's why we need to say row[0] to get the actual value
    # we are looking for. The tuple corresponds to what we ask for in the
    # sql statement. i.e., 'from_id' above or 'from_id,to_id' below 🤓

# find the ids that receive page rank
to_ids = []
links = []
cur.execute("select distinct from_id,to_id from links")
for row in cur:
    from_id = row[0]
    to_id = row[1]
    if from_id == to_id:
        continue
    if from_id not in from_ids:
        continue
    if to_id not in from_ids:
        continue
    links.append(row)
    if to_id not in to_ids:
        to_ids.append(to_id)

# get latest page ranks for strongly connected component
prev_ranks = {}
for node in from_ids:
    cur.execute("select new_rank from pages where id=?", (node,))
    row = cur.fetchone()
    prev_ranks[node] = row[0]

sval = input("how many iterations: ")
many = 1
if len(sval) > 0:
    many = int(sval)


# sanity check here
if len(prev_ranks) < 1:
    print("Nothing to page rank. Check the data.")
    quit()

# let's do page rank in memory so its really fast
for i in range(many):
    # print(prev_ranks.items()[:5])
    next_ranks = {}
    total = 0.0
    for node, old_rank in prev_ranks.items():
        total += old_rank
        next_ranks[node] = 0.0
    # print(total)

    # find the number of outbound links and send the page rank down each
    for node, old_rank in prev_ranks.items():
        # print(node,old_rank)
        give_ids = []
        for from_id, to_id in links:
            if from_id != node:
                continue
            # print('  ',from_id,to_id)

            if to_id not in to_ids:
                continue
            give_ids.append(to_id)
        if len(give_ids) < 1:
            continue
        amount = old_rank / len(give_ids)
        # print(node,old_rank,amount,give_ids)

        for id in give_ids:
            next_ranks[id] += amount

    newtot = 0
    for node, next_rank in next_ranks.items():
        newtot += next_rank
    evap = (total - newtot) / len(next_ranks)

    # print(newtot,evap)
    for node in next_ranks:
        next_ranks[node] += evap

    newtot = 0
    for node, next_rank in next_ranks.items():
        newtot += next_rank

    # compute the per-page average change from old rank to new rank
    # As indication of convergence of the algorithm
    totdiff = 0
    for node,old_rank in prev_ranks.items():
        new_rank=next_ranks[node]
        diff=abs(old_rank-new_rank)
        totdiff+=diff

    avediff=totdiff/len(prev_ranks)
    print(i+1,avediff)

    # rotate
    prev_ranks = next_ranks

# Put the final ranks back into the database
print(list(next_ranks.items())[:5])
cur.execute('update pages set old_rank=new_rank')
for id,new_rank in next_ranks.items():
    cur.execute('update pages set new_rank=? where id=?',(new_rank,id))
conn.commit()
cur.close()


