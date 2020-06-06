# Use the file name mbox-short.txt as the file name
c=0
tot=0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") :
		continue

	pos=line.rfind(' ')
	num=float(line[pos+1: ])
	tot=tot+num
	c=c+1
a=tot/c
print("Average spam confidence:",a)