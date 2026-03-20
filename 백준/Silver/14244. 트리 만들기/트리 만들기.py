import sys

# n개의 노드, m개의 리프트로 이루어져 있는 트리
n, m = map(int, sys.stdin.readline().strip().split(" "))

graph = []

for i in range(1,m+1):
    graph.append((0,i))

for j in range(m+1, n):
    graph.append((j-1, j))

# 남은 정점들은 마지막 리프 뒤에 차례대로 연결
last = m
for j in range(m + 1, n):
    graph.append((last, j))
    last = j

for a, b in graph:
    print(a, b)