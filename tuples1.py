name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
di =  dict()
    
for line in handle:
    if line.startswith("From "):
        words = line.rstrip().split()
        time = words[5].split(':')
        extr = time[0]
        di[extr] = di.get(extr, 0) + 1

li = list()
for k, v in di.items():
    tup = (k, v)
    li.append(tup)
    
for k, v in sorted(li):
    print(k, v)
