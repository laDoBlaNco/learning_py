# opengeo.py

"""
SERVICE ORIENTED APPROACH

• Most non-trivial web applications use services

• The use services from other applications
    • Credit Card Charge
    • Hotel Reservation systems

• Services publish the 'rules' applications must follow to make use of the
  service (API)

MULTIPLE SYSTEMS

• Initially - two systems cooperate and split the problem

• As the data/service becomes useful - multiple applications want to use the
  information / application

THERE ARE MANY APIS

• There are orgs that put up public APIs and sell access to those APIs

• We will explore a geocoding API based on the OpenStreetMap data

• You need an account to access this API

• There is a free level request

• You pay above that rate of usage


"""

from urllib import request, parse
import json
import ssl

serviceurl = "https://py4e-data.dr-chuck.net/opengeo?"

# ignore SSL cert errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


address = input("Enter location: ")
if len(address) < 1:
    address = "university of Patras"

address = address.strip()
parms = {}
parms["q"] = address

url = serviceurl + parse.urlencode(parms)

print("Retrieiving:", url)
uh = request.urlopen(url, context=ctx)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

js = json.loads(data)

print('Plus code',js['features'][0]['properties']['plus_code'])