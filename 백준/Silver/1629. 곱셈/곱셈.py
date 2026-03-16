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