# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

"""
일직선 위에 N개의 높이가 다른 탑 왼 -> 오 차례대로 세움
각 탑의 꼭대기에 레이저 송신기 설치, 레이저 왼쪽으로 발사
"""

import sys

n = int(sys.stdin.readline())
input = sys.stdin.readline().strip()

input_stack = input.split(" ")
result_stack = []

print(input_stack)

for i in range(len(input_stack)-1, -1, -1):
    target_num = input_stack.pop()
    print(f"꺼낸 숫자: {target_num}")

    for j in range(len(input_stack)-1, -1, -1):
        if input_stack[j] >= target_num:
            result_stack.append(j+1)
            break
    result_stack.append(0)
     

print(result_stack)

"""
5
6 9 5 7 4
['6', '9', '5', '7', '4']
꺼낸 숫자: 4
꺼낸 숫자: 7
꺼낸 숫자: 5
꺼낸 숫자: 9
꺼낸 숫자: 6
[4, 0, 2, 0, 2, 0, 0, 0]
"""

"""
동현 엣지 케이스

8
6 9 5 7 4 3 8 10
"""