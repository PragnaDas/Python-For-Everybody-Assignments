fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
bigcount=None
bigword=None
fh = open(fname)
counts = dict()
for line in fh:
	line = line.rstrip()
	if not line.startswith('From '): 
		continue
	words = line.split()
	word=words[5]
	nums=word.split(':')
	num=nums[0]
	counts[num]=counts.get(num,0)+1
hlst=list()
for k,v in counts.items():
	hlst.append((k,v))
hlst.sort()
for k,v in hlst:
	print(k,v)