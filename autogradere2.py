import re

hand = open('./assignment.txt')

x = list()

for line in hand:
    y = re.findall('[0-9]+',line)
    x = x+y
    print(y)
    print(x)

num = [int(x) for x in x]

sum = 0
for num in num:
    sum = sum + num

print (sum)