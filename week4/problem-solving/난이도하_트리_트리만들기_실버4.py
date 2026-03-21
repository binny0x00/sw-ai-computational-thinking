# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# 중심 노드에 새로 붙이면 리프 수 +1
# 기존 리프에 이어 붙이면 리프 수 유지

import sys

# n개의 노드, m개의 리프트로 이루어져 있는 트리
n, m = map(int, sys.stdin.readline().strip().split())

graph = []

for i in range(n-m):
    graph.append((0+i,i+1))

if graph:
    last_parent_node = graph[-1][1]
else:
    last_parent_node = 0

for j in range(1,m):
    graph.append((last_parent_node, last_parent_node+j))

for a, b in graph:
    print(a, b)