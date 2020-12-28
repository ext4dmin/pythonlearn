 #10.2 Напишите программу, которая прочитает mbox-short.txt
#и вычислит распределение по часам дня для каждого из сообщений.
#Вы можете вывести час из строки «От», найдя время,
#а затем разделив строку во второй раз, используя двоеточие.
#От stephen.marquard@uct.ac.za Сб, 5 января, 09:14:16 2008 г.
#После того, как вы накопите счетчики за каждый час,
#распечатайте счетчики, отсортированные по часам, как показано ниже.

import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_1036234.txt"
try:
    fh = open(fname)
except:
    print('Sorry, entered file name is not found.')
    quit()
res = 0
for i in (re.findall(('[0-9]+'),fh.read())):
    res = res+int(i)
print(res)
