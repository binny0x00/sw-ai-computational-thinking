import sys

# 이진 탐색
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) //2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0

n = int(sys.stdin.readline().strip())

A = list(map(int, sys.stdin.readline().strip().split(" ")))

# print(A)

m = int(sys.stdin.readline().strip())

M = list(map(int, sys.stdin.readline().strip().split(" ")))

A.sort()

for i in range(len(M)):
    result = binary_search(A, M[i])
    print(result)