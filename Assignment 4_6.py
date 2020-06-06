def computepay(h,r):
	if h>40 :
		p=40*r
		ad=(h-40)*1.5*r
		product=p+ad
	else:
		product=h*r
	return product

hrs=input("Enter Hours ")
h=float(hrs)
rate=input("Enter Per ")
r=float(rate)
print("Pay",computepay(h,r))