# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, rOrL):
            if not root:
                return 0
            left = dfs(root.left, "l")
            right = dfs(root.right, "r")
            if rOrL == "l" and not root.left and not root.right:
                return left + root.val
            else:
                return left + right
        return dfs(root, "")