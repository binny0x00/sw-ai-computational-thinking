# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914

n = int(input())
count = 0

print(2**n-1)

def hanoi(n, start, end, aux):
  if n<= 20:
    if n == 1:
      print(f"{start} {end}")
      return
  
    hanoi(n-1, start, aux, end)
    print(f"{start} {end}")
    hanoi(n-1, aux, end, start)
  

hanoi(n,1,3,2)