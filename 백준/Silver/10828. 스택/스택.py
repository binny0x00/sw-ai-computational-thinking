import sys

stack = []

n = int(sys.stdin.readline())

def action(s):
    temp = s.split(" ")
    
    if temp[0] == "push":
        stack.append(temp[1])
    elif temp[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif temp[0] == "size":
        print(len(stack))
    elif temp[0] == "empty":
        if stack:
            print(0)
        else : print(1)
    elif temp[0] == "top":
        if stack:
            print(stack[-1])
        else : print(-1)

for i in range(n):
    s = sys.stdin.readline().strip()
    action(s)