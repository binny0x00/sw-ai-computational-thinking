from collections import deque
import sys

def function(queue):
    while queue:
        if len(queue) == 1:
            print(queue.pop())
            return
        queue.popleft()
        queue.append(queue.popleft())


n = int(sys.stdin.readline().strip())

queue = deque()

for i in range(1,n+1):
    queue.append(i)

function(queue)