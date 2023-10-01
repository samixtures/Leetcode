# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        can be 0-100 nodes

        
        """
        returnList = []
        def traversal(root, returnList):
            if not root:
                return returnList
            traversal(root.left, returnList)
            returnList.append(root.val)
            traversal(root.right, returnList)
            return returnList
        return traversal(root, returnList)