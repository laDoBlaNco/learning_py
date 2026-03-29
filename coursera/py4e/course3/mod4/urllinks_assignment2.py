# urllinks_assignment2.py

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs  # type: ignore
import ssl  # this isn't necessary but its a hack around cert errors

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL: ")
ct = int(input("Enter count: "))
pos = int(input("Enter position: "))

print(f"Retrieving: {url}") 
for _ in range(ct):
    page = urlopen(url, context=ctx).read()
    page_tree = bs(page, "html.parser")

    # retrieve all of the anchor tags
    tags = page_tree("a")
    new_url = tags[pos-1].get('href',None)
    print(f"Retrieving: {new_url}")
    url = new_url
