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

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    address = address.strip()
    parms = {}
    parms["q"] = address

    url = serviceurl + parse.urlencode(parms)

    print("Retrieiving:", url)
    uh = request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters", data[:20].replace("\n", " "))

    js = json.loads(data)

    lat = js["features"][0]["properties"]["lat"]
    lon = js["features"][0]["properties"]["lon"]
    print("lat:", lat, "lon:", lon)
    location = js["features"][0]["properties"]["formatted"]
    print(location)

    '''
    SUMMARY

    • Service Oriented Architecture - allows an application to be broken
      into parts an distributed across a network

    • An Application Program Interface (API) is a contract for interaction

    • Web Services provide infrastructures for applications cooperating
      (an API) over a network - SOAP and REST are two styles of web 
      services

    • XML and JSON are serialization formats

    
    '''
