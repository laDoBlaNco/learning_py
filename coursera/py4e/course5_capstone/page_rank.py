# page_rank.py

#  PAGE RANK
#
# • We will write a simple web page crawler
#
# • Compute a simple version of Google's Page Rank algorithm
#
# • Visualize the resulting network

# WEB CRAWLER
#
# A web crawler is a compuer program that browses the web in a methodical
# automated manner. Web crawlers are mainly used to create a copy of all
# the visited pages for later processing by a search engine that will index
# teh downloaded pages to provide fast searches.

# • Retrieve page
# • Look through the page for links
# • add the links to a list of 'to be retrieved' sites
# • repeat...

# REAL WORLD WEB CRAWLING POLICY
#
# • a selection policy taht states which pages to download
# • A re-visit policy that states when to check for changes to those pages
# • a politeness policy that states how to avoid overloading web sites, and
# • a parallelization policy that states how to coordinate distributed Web
#   crawlers

# ROBOTS.TXT
#
# • a way for a web site to communicate with web crawlers
#   • user-agent: * or Disallow: /cgi-bin/ and Disallow: /images/, etc.
# • an informal and voluntary standard
# • sometimes folks make a 'spider trap' to catch 'bad' spiders
# • http://en.wikipedia.org/wiki/Robots_Exclusion_Standard
# • http://en.wikipedia.org/wiki/Spider_trap

# SEARCH INDEXING
#
# Search engine indexing collects, parses, and stores data to faciliate fast
# and accuratee information retrieval. The purpose of storing an index is
# to optimize speed and performance in finding relevant documents for a search
# query. Without an index, the search engine would scan every document in the
# corpus, which would require considerable time and computing power.
# http://en.wikipedia.org/wiki/index_(search_engine)


