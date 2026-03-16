import sys

def calculate_squre(num, num2, num3):
    if num2 == 1:
        return num % num3
    
    if num2 == 2:
        return (num ** 2) % num3
    
    if num2 % 2 == 0:
        return ((calculate_squre(num, num2//2, num3)) ** 2) % num3
    else:
        return (num * (calculate_squre(num, (num2-1)//2, num3)) ** 2) % num3
    
input_list = sys.stdin.readline().strip().split(" ")

squred_num = calculate_squre(int(input_list[0]), int(input_list[1]), int(input_list[2]))
print(squred_num)