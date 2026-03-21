import sys

# n개의 노드, m개의 리프트로 이루어져 있는 트리
n, m = map(int, sys.stdin.readline().strip().split())

graph = []

for i in range(n-m):
    graph.append((0+i,i+1))

last_parent_node = graph[-1][1]

for j in range(1,m):
    graph.append((last_parent_node, last_parent_node+j))

for a, b in graph:
    print(a, b)