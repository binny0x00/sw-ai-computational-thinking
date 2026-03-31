import sys

def count_new_player(score_list):
    count = 0
    # meetings = sorted(meetings, key=lambda x: x[1])
    score_list = sorted(score_list, key=lambda x: x[0])

    a, b = score_list[0]
    count += 1

    for i in range(1,len(score_list)):
        c, d = score_list[i]
        if a > c or b > d:
            a, b = c, d
            count += 1

    return count

input = sys.stdin.readline

T = int(input())
scores = [[] for _ in range(T)]
for i in range(T):
    N = int(input())
    for j in range(N):
        a, b = map(int,input().split())
        scores[i].append([a,b])
    # print(scores[i])
    print(count_new_player(scores[i]))