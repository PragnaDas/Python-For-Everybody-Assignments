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
	word=words[1]
	counts[word]=counts.get(word,0)+1
for key,count in counts.items():
	if bigcount is None or count > bigcount:
		bigcount=count
		bigword= key

print(bigword,bigcount)