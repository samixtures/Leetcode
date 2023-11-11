# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(root, sum):
            if not root:
                return 0
            sumOfNum = 0
            left, right = 0, 0
            if root.left:
                left += root.left.val
            if root.right:
                right += root.right.val
            sumOfNum += abs(left - right)
            newLeft = dfs(root.left, sumOfNum)
            newRight = dfs(root.right, sumOfNum)
            return sumOfNum + newLeft + newRight
        return dfs(root, 0)