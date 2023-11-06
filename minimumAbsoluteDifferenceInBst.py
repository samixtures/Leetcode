# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # are all node values unique? -> important bcz 3 - 3 = 0

        s = set()
        def dfs(root, minDif):
            if not root:
                return None
            if root.val not in s:
                for x in s:
                    minDif = min(abs(x-root.val), minDif)
                s.add(root.val)
            left = dfs(root.left, minDif)
            right = dfs(root.right, minDif)
            if left and right:
                smallest = min(left, right)
            elif left:
                smallest = left
            elif right:
                smallest = right
            else:
                return minDif
            return min(minDif, smallest)
        return dfs(root, float('inf'))
