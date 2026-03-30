# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

import sys

def fibo(n, memo=None):
    if memo is None:
        memo = {0:0, 1:1}

    if n in memo:
        return memo[n]
    
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

n = int(sys.stdin.readline())
print(fibo(n))