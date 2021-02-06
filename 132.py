# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_1036239.json (Sum ends with 12)

import urllib.request
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    adress = input("Enter URL: ")
    if len(adress) < 0:
        break
    summ = 0
    cont = urllib.request.urlopen(adress, context=ctx).read().decode('utf-8')
    js = json.loads(cont)
    for j in js["comments"]:
        summ = summ + int(j['count'])
    print(summ)
