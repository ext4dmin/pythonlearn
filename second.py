largest = None
smallest = None
while True:
    try:
        num = int(input("Enter a number: "))
    except:
        print ("Invalid input")

    if num == "done" : break

    if largest == None:
        largest = num
    if smallest == None:
        smallest = num

    if largest < num:
        largest = num
    elif smallest > num:
        smallest = num

print("Maximum", largest)
print("Minimum", smallest)
