# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            if root1 and root2:
                newRoot = TreeNode(root1.val+root2.val)
                newRoot.left = dfs(root1.left, root2.left)
                newRoot.right = dfs(root1.right, root2.right)
                return newRoot
            else:
                return root1 or root2
        return dfs(root1, root2)