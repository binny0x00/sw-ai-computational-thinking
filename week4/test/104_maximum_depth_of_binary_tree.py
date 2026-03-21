# 문제 링크: : https://leetcode.com/problems/maximum-depth-of-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 트리의 깊이를 재귀의 반환값으로 계산
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1