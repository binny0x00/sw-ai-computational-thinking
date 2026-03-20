# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# root: n, root.left:2n, root.left:2n+1

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 다음 순서로 들어갈 node 저장
        list = []
        depth = 0

        while root:
            if root.left is None:
                if list:
                    root = list[-1]
            else:
                depth += 1
                if root.left:
                    list.append(root.left)
                else:
                    list.append(root.right)

            list.pop()
            if list:
                root = list[-1]
        
        return depth