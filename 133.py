
import urllib.request, urlib.parse, urlib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    adress = input("Enter adress: ")
    if len(adress) < 0:
        break

    summ = 0
    cont = urllib.request.urlopen(adress, context=ctx).read().decode('utf-8')
    js = json.loads(cont)
    for j in js["comments"]:
        summ = summ + int(j['count'])
    print(summ)
