import sys

input = []

N = int(sys.stdin.readline())
for i in range(N):
    s = sys.stdin.readline().strip()
    input.append(s)

for s in input:
    sys.stdout.write(s)