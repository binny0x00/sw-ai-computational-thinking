# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

import sys
from collections import deque

input = sys.stdin.readline

# 게임 구역의 크기
n = int(input())

game_board = []

for _ in range(n):
    row = list(map(int, input().split()))
    game_board.append(row)

# 방문 여부 체크
visit = []
for _ in range(n):
    visit.append([False]*n)

dx = [1,0]
dy = [0,1]

def bfs(x, y, visit):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = True

    while queue:
        x,y = queue.popleft()
        jump = game_board[x][y]

        if jump == -1:
            return "HaruHaru"
        
        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump
            
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False:
                visit[nx][ny] = True
                queue.append((nx,ny))
    return "Hing"

print(bfs(0,0,visit))