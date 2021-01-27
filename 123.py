#  Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1).
# Follow that link. Repeat this process 4 times.
# The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Tanzina.html
# Find the link at position 18 (the first name is 1).
# Follow that link. Repeat this process 7 times.
# The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: A

from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
repeat_proc = int(input('Enter count repeat: '))-1
position_num = int(input('Enter position: '))-1

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tag = soup.find_all('a', limit=position_num+1)

while repeat_proc > 0:
    repeat_proc = repeat_proc-1
    html = urlopen(tag[position_num].get('href'), context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find_all('a', limit=position_num+1)
print(tag[position_num].contents)
