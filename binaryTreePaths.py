# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root, path, retList):
            if not root:
                return
            path += str(root.val) + "->"
            if not root.left and not root.right:
                retList.append(path[:-2])
            dfs(root.left, path, retList)
            dfs(root.right, path, retList)
        retList = []
        dfs(root, "", retList)
        return retList
        