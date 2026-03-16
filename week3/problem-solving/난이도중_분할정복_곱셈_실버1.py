# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

import sys

def calculate_squre(num, num2, num3):
    if num2 == 1:
        return num % num3
    
    if num2 == 2:
        return (num ** 2) % num3
    
    if num2 % 2 == 0:
        return ((calculate_squre(num, num2//2, num3)) ** 2) % num3
    else:
        return (num * ((calculate_squre(num, (num2-1)//2, num3)) ** 2)) % num3
    
a,b,c= map(int, sys.stdin.readline().strip().split(" "))

squred_num = calculate_squre(a, b, c)
print(squred_num)