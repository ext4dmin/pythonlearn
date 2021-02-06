#  Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1036238.xml (Sum ends with 10)

import urllib.request
import ssl
import xml.etree.ElementTree as ET

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
if api_key is False:
    api_key = 42
    serviceurl =  serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
summ = 0
while True:
    adress = input("Enter URL: ")
    if len(adress) < 0:
        break
    cont = urllib.request.urlopen(adress, context=ctx).read()
    tree = ET.fromstring(cont)
    results = tree.findall('.//count')
    for res in results:
        summ = summ + int(res.text)
    print(summ)
