# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933
import sys

n = int(sys.stdin.readline().strip())

input_list = set()

for i in range(n):
    input_list.add(sys.stdin.readline().strip())

for target in input_list:
    # print(target[::-1])

    if target[::-1] in input_list:
        print(f"{len(target)} {target[len(target)//2]}")
        break