# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
root
root.left.val + root.right.val
root.left.left.val + root.left.right.val + root.right.left.val + root.right.right.val
"""

class Solution:
    result = []
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is not None:
            # 1번 노드 추가
            if len(self.result) == 0:
                self.result.append(float(root.val))
            # 자식 노드 평균 리스트에 추가하기 (재귀)
            sum = 0
            count = 0
            if root.left is not None:
                sum += root.left.val
                count += 1
            if root.right is not None:
                count += 1
                sum += root.right.val
            
            if count > 0:
                self.result.append(float((sum)/count))

                self.averageOfLevels(root.left)
                self.averageOfLevels(root.right)

            return self.result
        return self.result
    
"""
Case 1: SUCCESS
expected: [3.00000,14.50000,11.00000]
actual:   [3.00000,14.50000,11.00000]

Case 2: FAIL
expected: [3.00000,14.50000,11.00000]
actual:   [3.00000,14.50000,11.00000,14.50000,11.00000]

"""