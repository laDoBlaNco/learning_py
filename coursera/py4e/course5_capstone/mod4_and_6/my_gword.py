# my_gword.py

import sqlite3
import string

conn = sqlite3.connect("my_index.sqlite")
cur = conn.cursor()

cur.execute("select id,subject from subjects")
subjects = {}
for message_row in cur:
    subjects[message_row[0]] = message_row[1]

cur.execute("select subject_id from messages")
counts = {}
for message_row in cur:
    text = subjects[message_row[0]]
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.translate(str.maketrans("", "", "1234567890"))
    text = text.strip().lower()
    words = text.split()
    for word in words:
        if len(word) < 4:
            continue
        counts[word] = counts.get(word, 0) + 1

x = sorted(counts, key=counts.get, reverse=True)
highest = None
lowest = None
for k in x[:100]:
    if highest is None or highest < counts[k]:
        highest = counts[k]
    if lowest is None or lowest > counts[k]:
        lowest = counts[k]


print(f"Range of counts: {highest} <--> {lowest}")

# spread the font sizes across 20-100 based on the count
bigsize = 80
smallsize = 20

fhand = open("my_gword.js", "w")
fhand.write("gword = [")
first = True
for k in x[:100]:
    if not first:
        fhand.write(",\n")
    first = False
    size = counts[k]
    size = (size - lowest) / float(highest - lowest)
    size = int((size * bigsize) + smallsize)
    fhand.write("{text: '" + k + "', size: " + str(size) + "}")
fhand.write("\n];\n")

print("Output written to my_gword.js")
print("Open my_gword.htm in a browser to see the visualization")
