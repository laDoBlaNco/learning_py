# urllinks.py

import urllib.request
from bs4 import BeautifulSoup as bs  # type: ignore
import ssl  # this isn't necessary but its a hack around cert errors

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = bs(html, "html.parser")

# retrieve all of the anchor tags
tags = soup("a")
print(tags)
for tag in tags:
    print(tag.get("href", None))
