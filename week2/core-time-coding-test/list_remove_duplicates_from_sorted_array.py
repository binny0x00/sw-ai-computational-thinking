#link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 1

        while right < len(nums) and left < right:
            if nums[left] == nums[right]:
                nums.pop(nums[right])
                continue
            else:
                left +=1
                right +=1

        k = len(nums)

        return k
        

"""
nums: 내림차순 정렬된 정수 배열
중복을 제거하되 원본 배열을 변경하지 않아야 함

k: 중복 제거 후 고유 요소 개수
"""
        

# Case 1
# Input
# nums = [1,1,2]
# Output
# [1,2]

# Case 2
# Input
# nums = [0,0,1,1,1,2,2,3,3,4]
# Output
# [0,1,1,2,3,4]