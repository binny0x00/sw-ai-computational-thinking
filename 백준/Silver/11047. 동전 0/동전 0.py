import sys

n, k = map(int, sys.stdin.readline().strip().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# 큰 순서대로 정렬
coins = sorted(coins, reverse=True)
total_count = 0

for coin in coins:
    count = k // coin
    total_count += count
    k %= coin

print(total_count)