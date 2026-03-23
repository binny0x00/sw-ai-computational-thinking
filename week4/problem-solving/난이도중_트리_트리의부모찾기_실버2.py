# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

import sys
from collections import deque

# 노드의 개수
n = int(sys.stdin.readline().strip())

# 노드랑 index를 맞추기 위해서 0번지는 비움
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# 부모 노드를 저장할 리스트 생성
parent = [0] * (n + 1)
parent[1] =  -1 # 루트 표시

# 문제에서 트리의 루트를 1이라고 정했기 때문에 트리를 생성과 동시에 초기화
queue = deque([1])

while queue:
    current = queue.popleft()
    for next_node in graph[current]:
        if parent[next_node] == 0:
            parent[next_node] = current
            queue.append(next_node)

for i in range(2, n+1):
    print(parent[i])