# my_spider.py

import sqlite3
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs  # type: ignore

# ignore the ssl certificate trick
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect("my_spider.sqlite")
cur = conn.cursor()

cur.execute("""create table if not exists Pages
            (id integer primary key, url text unique, html text,
            error integer, old_rank real, new_rank real)""")

cur.execute("""create table if not exists Links
            (from_id integer, to_id integer)""")

cur.execute("create table if not exists Webs (url text unique)")

# now let's check to see if we are already in progress...
cur.execute(
    "select id,url from Pages where html is null and error is null order by random() limit 1"
)
row = cur.fetchone()
if row is not None:
    print("Restarting existing crawl. Remove spider.sqlite to start a fresh")
else:
    starturl = input("Enter web url or enter: ")
    if len(starturl) < 1:
        starturl = "https://www.dr-chuck.com"
    if starturl.endswith("/"):
        starturl = starturl[:-1]
    web = starturl
    if starturl.endswith(".htm") or starturl.endswith(".html"):
        pos = starturl.rfind("/")
        web = starturl[:pos]

    if len(web) > 1:
        cur.execute("insert or ignore into Webs (url) values (?)", (web,))
        cur.execute(
            "insert or ignore into Pages (url,html,new_rank) values(?,null,1.0)",
            (starturl,),
        )
        conn.commit()

# get the current webs
cur.execute("select url from webs")
webs = []
for row in cur:
    webs.append(str(row[0]))

print(webs)

many = 0
while True:
    if many < 1:
        sval = input("How many pages: ")
        if len(sval) < 1:
            break
        many = int(sval)
    many -= 1

    cur.execute(
        "select id,url from pages where html is null and error is null order by random() limit 1"
    )
    try:
        row = cur.fetchone()
        print(row)
        fromid = row[0]
        url = row[1]
    except:  # noqa: E722
        print("No unretrieved HTML pages found")
        many = 0
        break

    print(fromid, url, end=" ")

    # if we are retrieving this page, there shoudl be no links from it already
    cur.execute("delete from links where from_id=?", (fromid,))
    try:
        document = urlopen(url, context=ctx)
        html = document.read()
        if document.getcode() != 200:
            print(f"Error on page: {document.getcode()}")
            cur.execute(
                "update pages set error=? where url=?", (document.getcode(), url)
            )

        if "text/html" != document.info().get_content_type():
            print("Ignore  non text/html page")
            cur.execute("delete from pages where url=?", (url,))
            cur.execute("update pages set error=0 where url=?", (url,))
            conn.commit()
            continue

        print(f"({str(len(html))})", end=" ")

        soup = bs(html, "html.parser")
    except KeyboardInterrupt:
        print("")
        print("Program interrupted by user...")
        break
    except:  # noqa: E722
        print("Unable to retrieve or parse page")
        cur.execute("update pages set error=-1 where url=?", (url,))
        conn.commit()
        continue

    cur.execute(
        "insert or ignore into pages(url,html,new_rank) values(?,null,1.0)", (url,)
    )
    cur.execute("update pages set html=? where url=?", (memoryview(html), url))
    conn.commit()

    tags = soup("a")
    count = 0
    for tag in tags:
        href = tag.get("href", None)
        if href is None:
            continue
        # resolve relative refs like href='/contact'
        up = urlparse(href)
        if len(up.scheme) < 1:
            href = urljoin(url, href)
        ipos = href.find("#")
        if ipos > 1:
            href = href[:ipos]
        if href.endswith(".png") or href.endswith(".jpg") or href.endswith(".gif"):
            continue
        if href.endswith("/"):
            href = href[:-1]
            # print(href)
        if len(href) < 1:
            continue

        # check if the url is in any of the webs
        found = False
        for web in webs:
            if href.startswith(web):
                found = True
                break
        if not found:
            continue

        cur.execute(
            "insert or ignore into pages (url,html,new_rank) values(?,null,1.0)",
            (href,),
        )
        count += 1
        conn.commit()

        cur.execute("select id from pages where url=? limit 1", (href,))
        try:
            row = cur.fetchone()
            toid = row[0]
        except:  # noqa: E722
            print("Could not retrieve id")
            continue

        # print(fromid,toid)
        cur.execute(
            "insert or ignore into links (from_id,to_id) values(?,?)", (fromid, toid)
        )

    print(count)

cur.close()
