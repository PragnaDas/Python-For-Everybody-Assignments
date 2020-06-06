fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	word=line.split()
	for i in word:
		if i in lst:
			continue
		lst.append(i)
lst.sort()
print(lst)