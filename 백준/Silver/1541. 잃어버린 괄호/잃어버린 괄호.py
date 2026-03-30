import sys

# [55, 50+40]
n = sys.stdin.readline().strip().split('-')

numbers = []

for str in n:
    if "+" in str:
        temp = map(int,str.split('+'))
        sum = 0
        for num in temp:
            sum += num
        numbers.append(sum)
    else:
        numbers.append(int(str))
res = numbers[0]
for i in range(1,len(numbers)):
    res -= numbers[i]

print(res)