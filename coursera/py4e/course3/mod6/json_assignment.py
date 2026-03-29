# json_assignment.py

from urllib import request
import json
import ssl

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter Location: ")
if len(url)<1:
    url = "http://py4e-data.dr-chuck.net/comments_2152094.json"
print('Retrieving',url)

uh = request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved",len(data),"characters")

js = json.loads(data)
counts = []
for item in js['comments']:
    counts.append(int(item['count']))

print("Count:",len(js['comments']))
print('Sum:',sum(counts))