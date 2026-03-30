import sys

def fibo(n, memo=None):
    if memo == None:
        memo = {0:0, 1:1}

    if n in memo:
        return memo[n]
    
    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]

input = int(sys.stdin.readline())
print(fibo(input))