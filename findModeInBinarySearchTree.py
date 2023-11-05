# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        def dfs(root):
            if not root:
                return None
            if root.val not in freq:
                freq[root.val] = 1
            else:
                freq[root.val] += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)

        modes = []
        maxVal = float('-inf')
        for x in freq:
            if freq[x] > maxVal:
                maxVal = freq[x]
        for x in freq:
            if freq[x] == maxVal:
                modes.append(x)
        return modes