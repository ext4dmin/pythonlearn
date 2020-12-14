# 8.5 Откройте файл mbox-short.txt и прочтите его построчно.
#Когда вы найдете строку, начинающуюся с "От", например, следующую строку:
#От stephen.marquard@uct.ac.za Сб, 5 января, 09:14:16 2008 г.
#Вы проанализируете строку «От» с помощью split () и
#распечатаете второе слово в строке (т.е. весь адрес человека, отправившего сообщение).
#Затем распечатайте счетчик в конце.
#Подсказка: не включайте строки, начинающиеся с "От:".
#Также посмотрите на последнюю строку выходных данных, чтобы узнать, как распечатать счетчик.

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except:
    print('Sorry, entered file name is not found.')
    quit()
counter = 0
maillist = list()

for str in fh:
    str = str.rstrip()
    if not str.startswith("From "):continue
    str = str.split()
    maillist.append(str[1])
    counter = counter + 1
for mail in maillist : print(mail)
print("There were",counter,"lines in the file with From as the first word")
