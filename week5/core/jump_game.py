# 링크 : https://leetcode.com/problems/jump-game/description/

"""
nums : 정수 배열
첫 번째 인덱스 초기 위치
배열의 각 요소는 해당 위치에서 최대 점프 거리

마지막 인덱스에 도달할 수 있으면 true, 없으면 false 반환
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0    # 가장 멀리 갈 수 있는 위치 기록

        for i in range(len(nums)):
            if i > max_distance:
                return False
            
            max_distance = max(max_distance, i + nums[i])
        
        return True