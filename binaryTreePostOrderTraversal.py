# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        left always comes before right
        in this case I believe it's left, right, root
        """
        returnList = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            returnList.append(root.val)
            return
        helper(root)
        return returnList