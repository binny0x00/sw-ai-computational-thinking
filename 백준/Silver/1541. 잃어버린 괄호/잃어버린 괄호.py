import sys

# [55, 50+40]
expression = sys.stdin.readline().strip().split('-')

numbers = []

for group in expression:
    total = sum(map(int,group.split('+')))
    numbers.append(total)
    
res = numbers[0]
for i in range(1,len(numbers)):
    res -= numbers[i]

print(res)