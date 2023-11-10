"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root:
                return 0
            childr = root.children
            childrList = []
            for x in childr:
                childrList.append(dfs(x))
            if childrList:
                maxChild = max(childrList)
            else:
                maxChild = 0
            return 1 + maxChild
        return dfs(root)