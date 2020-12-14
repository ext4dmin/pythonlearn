# 8.4 Откройте файл romeo.txt и прочтите его построчно.
# Для каждой строки разделите строку на список слов с помощью метода split ().
# Программа должна составить список слов. Для каждого слова в каждой строке проверьте,
# есть ли слово уже в списке, и, если нет, добавьте его в список.
# Когда программа завершится, отсортируйте
# и распечатайте полученные слова в алфавитном порядке.

fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('Sorry, entered file name is not found.')
    quit()
str2list = list()
for str in fh:
    str = str.rstrip()
    slicestr = str.split()
    str2list = str2list + slicestr
retlist = list()
for ret in str2list:
    if ret not in retlist:
        retlist.append(ret)
print(sorted(retlist))
