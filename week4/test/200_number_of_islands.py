from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 그리드 m * n
        m = len(grid)
        n = len(grid[0])

        land = "1"
        water = "0"

        dx = [0, 1]
        dy = [1, 0]

        # # 모두 물인 경우
        # if sum(grid) == 0:
        #     return 0
        # # 모두 육지인 경우 (물이 아예 없어도 섬으로 count하는지 애매)
        # elif sum(grid) == m*n:
        #     return 1

        current_index = (0,0)
        queue = deque([current_index])
        visited = [[False]*n for i in range(m)]
        count = 1

        while queue:
            current = queue.popleft()
            current_value = grid[current[0]][current[1]]
            visited[current[0]][current[1]] = True

            # 모든 노드 탐색
            for i in range(2):
                if visited[current_index[0]+dx[i]][current_index[1]+dy[i]] is False:
                    queue.append((current_index[0]+dx[i], current_index[1]+dy[i]))
                    visited[current_index[0]+dx[i]][current_index[1]+dy[i]] = True

            # 같은 value를 가진 구역이 총 몇개로 나눠지는 지 확인