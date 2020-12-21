# 9.4 Напишите программу для чтения mbox-short.txt и выяснения,
#кто отправил наибольшее количество почтовых сообщений.
#Программа ищет строки "От" и принимает второе слово из этих строк как имя
#человека, отправившего письмо. Программа создает словарь Python,
#который сопоставляет почтовый адрес отправителя с количеством раз,
#которое они появляются в файле. После создания словаря программа
#читает словарь, используя максимальный цикл,
#чтобы найти наиболее плодовитого коммиттера.
#cwen@iupui.edu 5

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
    str = str.split()
    tex2list.append(str)

lis2dic = dict()
for li in tex2list:
    lis2dic[li[1]] = lis2dic.get(li[1],0) + 1

bigword = None
bigcount = None
for word,count in lis2dic.items():
    if bigword is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword,bigcount)
