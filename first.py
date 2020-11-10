def computepay(h,r):
    if h>40:
        res = 40*r + (h-40)*1.5*r
    else:
        res = h*r
    return res
def inputdata(param):
    return float(input("Enter "+str(param)+":"))

hrs = inputdata("Hours")
rate = inputdata("Rate")

p = computepay(hrs,rate)
print("Pay",p)
