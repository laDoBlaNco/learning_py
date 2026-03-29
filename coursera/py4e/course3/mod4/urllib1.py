# urllib1.py

# import urllib.request, urllib.parse, urllib.error  # noqa: E401

#not sure why chuck has us import all of these since we are only using the 
# the one. I also tried to just import the package, but then it python
# doesn't see the individual files. Possibly the difference of using packages
# vs modules. urllib is a package and urllib.request is the module
import urllib.request


fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())
