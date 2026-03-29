# urllinks_assignment.py

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs  # type: ignore
import ssl  # this isn't necessary but its a hack around cert errors

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = bs(html, "html.parser")

# retrieve all of the anchor tags
tags = soup("span")
tag_values = []
for tag in tags:
    # print(tag)
    tag_values.append(int(tag.contents[0]))

print(f"Count {len(tag_values)}")
print(f"Sum {sum(tag_values)}")
