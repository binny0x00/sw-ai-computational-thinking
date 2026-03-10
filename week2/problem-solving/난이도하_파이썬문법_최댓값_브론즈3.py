# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

# nums = []
# for i in range(9):
#   nums.append(int(input()))

# temp = nums.copy()
# temp.sort()
# print(temp[-1])

# for j in range(9):
#   if nums[j] == temp[-1]:
#     print(j+1)

nums = []
for i in range(9):
  nums.append(int(input()))

max_num = max(nums)

print(nums.index(max_num)+1)