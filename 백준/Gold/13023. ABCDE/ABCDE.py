import sys

def solution():
    input = sys.stdin.readline

    # n: 총 참가 인원, m: 친구 관계의 수
    n,m = map(int, input().split())

    # 0~ a~와 매칭
    graph = [[] for _ in range(n)]

    for _ in range(m):
        name1, name2 = map(int, input().split())
        graph[name1].append(name2)
        graph[name2].append(name1)

    history = [False]*n

    # 모든 사람에 대해서 연속해서 4개의 연결관계가 있는 부분이 있는지 확인해야 함
    # depth: 몇 번 이동했는지
    def dfs(node, depth):
        if depth == 4:
            return True
        
        for next_node in graph[node]:
            if not history[next_node]:
                history[next_node] = True
                if dfs(next_node, depth + 1):
                    return True
                history[next_node] = False

        return False

    for i in range(n):
        history[i] = True
        if dfs(i,0):
            return True
        history[i] = False
    
    return False

if solution():
    print(1)
else:
    print(0)