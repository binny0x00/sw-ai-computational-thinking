import sys
from collections import deque

input = sys.stdin.readline

computer_num = int(input())

n = int(input())

# 컴퓨터 번호와 인덱스를 맞추기 위해 0번지는 비워 놓음
computer = [[] for _ in range(computer_num+1)]

for _ in range(n):
    a,b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

queue = deque([1])
history = [False for _ in range(computer_num+1)]

while queue:
    current = queue.popleft()
    if not history[current]:
        history[current] = True
        for next_node in computer[current]:
            if not history[next_node]:
                queue.append(next_node)

print(sum(history)-1)