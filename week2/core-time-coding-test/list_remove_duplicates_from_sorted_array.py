class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 중복된 숫자 제거 (오름차순 정렬 됨, 그자리에서 제거)
        for x in range(len(nums)):
            for y in range(len(nums[x+1:])):
                if x+1+y < len(nums) and nums[x] == nums[x+1+y]:
                    nums.pop(x+1+y)

                    # 줄어드는 인덱스를 반영하지 못함
        
        # k = 고유 요소 개수
        k = len(nums)

        return k
        

# Case 1
# Input
# nums = [1,1,2]
# Output
# [1,2]
# Expected
# [1,2]

# Case 2
# Input
# nums = [0,0,1,1,1,2,2,3,3,4]
# Output
# [0,1,1,2,3,4]
# Expected
# [0,1,2,3,4]