# urllinks.py

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
tags = soup("a")
for tag in tags:
    # look at the different parts of the tag
    print('TAG:',tag)
    print('URL:',tag.get('href',None))
    print('Contents:',tag.contents[0])
    print('Attrs:',tag.attrs)
