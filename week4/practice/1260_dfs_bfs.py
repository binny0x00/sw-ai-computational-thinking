# 문제 : https://www.acmicpc.net/problem/1260
# DFS, BFS 구현

import sys
from collections import deque

input = sys.stdin.readline

# n: 정점 개수
# m : 간선 개수
# v : 탐색을 시작할 정점의 번호
n, m, v = map(int, input().split())

# 정점과 index의 숫자를 맞추기 위해서 1부터 사용
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    # 양방향 간선
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

# 방문할 수 있는 정점이 여러 개인 경우에 정점 번호가 작은 것을 먼저 방문
visited_dfs = [False] * (n+1)

res_dfs = []

def dfs(v):
    visited_dfs[v] = True
    res_dfs.append(v)

    graph[v].sort()
    for next_node in (graph[v]):
        if not visited_dfs[next_node]:
            dfs(next_node)


def bfs(v):
    res_bfs = []
    queue_bfs = deque([v])
    visited_bfs = [False] * (n+1)
    visited_bfs[v] = True

    while queue_bfs:
        current_node = queue_bfs.popleft()
        res_bfs.append(current_node)

        graph[current_node].sort()
        for next_node in (graph[current_node]):
            if not visited_bfs[next_node]:
                queue_bfs.append(next_node)
                visited_bfs[next_node] = True
    return res_bfs

dfs(v)
print(*res_dfs)
print(*bfs(v))