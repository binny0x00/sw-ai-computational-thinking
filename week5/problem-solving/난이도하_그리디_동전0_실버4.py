# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

import sys

n, k = map(int, sys.stdin.readline().strip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# 큰 순서대로 정렬
total_count = 0

for coin in reversed(coins):
    count = k // coin
    total_count += count
    k %= coin

print(total_count)