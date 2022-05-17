def computepay(h, r):
    if h > 40:
        p = (40 * r) + (h-40) * 1.5 * r 
    else:
        p = (h * r)
    return p

try:
	hrs = float(input("Enter Hours:"))
	rate = float(input("Enter Rate:"))
except:
    print("please enter a float")
    
print("Pay", computepay(hrs, rate))