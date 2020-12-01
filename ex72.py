fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print('Sorry, entered file name is not found.')
    quit()
count = 0.0000
spam = 0.0000
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        spline = float(line[(line.find(' ')):])
        spam = spam + spline
        count = count + 1

aver = spam/count
print('Average spam confidence:', aver)
