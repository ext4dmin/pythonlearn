 #10.2 Напишите программу, которая прочитает mbox-short.txt
#и вычислит распределение по часам дня для каждого из сообщений.
#Вы можете вывести час из строки «От», найдя время,
#а затем разделив строку во второй раз, используя двоеточие.
#От stephen.marquard@uct.ac.za Сб, 5 января, 09:14:16 2008 г.
#После того, как вы накопите счетчики за каждый час,
#распечатайте счетчики, отсортированные по часам, как показано ниже.


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('Sorry, entered file name is not found.')
    quit()
tex2list = list()
for str in fh:
    str = str.rstrip()
    if not str.startswith("From "):continue
    str = str.split(":")
    tex2list.append(str)


lis2dic = dict()
for li in tex2list:
    le = li[len(li)-3]
    lis2dic[le[len(le)-2:]] = lis2dic.get(le[len(le)-2:],0) + 1

res = sorted([(k,v) for k,v in lis2dic.items()])
for f,ff in res:
    print(f,ff)
