#link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = 1
        input_index = 1

        for current in range(1, len(nums)): # 빈 리스트, 길이 1 배열도 안전하게 처리 됨
            if nums[current] != nums[input_index-1]:
                nums[input_index] = nums[current]
                input_index +=1

        k = input_index

        return k

"""
리스트와 배열 차이

"""
"""
nums: 오름차순 정렬된 정수 배열
원본 배열 내부에서 중복 원소를 제거해야함

k: 중복 제거 후 고유 요소 개수
"""

"""
이 문제의 핵심은 유니크한 값을 앞쪽에 모으는 것
"""