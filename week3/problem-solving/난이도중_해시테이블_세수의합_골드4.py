# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
import sys

n = int(sys.stdin.readline().strip())

input_list = []
input_set = set()

# a+b
added_num = set()

# list와 set에 입력값 할당하기
for i in range(n):
    item = int(sys.stdin.readline().strip())
    input_set.add(item)
    input_list.append(item)

for x in range(n):
    for y in range(n):
        added_num.add(input_list[x]+input_list[y])
        continue

# print(added_num)

result = 0

for k in input_list:
    for c in input_list:
        if k - c in added_num:
            if result < k:
                result = k

if result > 0:
    print(result)