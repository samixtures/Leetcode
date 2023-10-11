# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        can have 0 nodes

        Given a binary tree
        Preorder: root, left, right?
        Inorder:left, root, right
        Postorder: left, right, root?

        I think left always comes before right

        Since we're returning a list I think we'll need a helper function
        """
        returnList = []
        def helper(root):
            if not root:
                return
            # print(root.val)
            returnList.append(root.val)
            helper(root.left)
            helper(root.right)
            return
        # print(helper(root))
        helper(root)
        return returnList