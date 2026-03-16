# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

# 시간초과 -> 이분탐색으로 수정해야 함

import sys

n = int(sys.stdin.readline().strip())

A = sys.stdin.readline().strip().split(" ")

# print(A)

m = int(sys.stdin.readline().strip())

M = sys.stdin.readline().strip().split(" ")

for i in range(len(M)):
    if M[i] in A:
        print("1")
    else:
        print("0")