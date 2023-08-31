# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(root):
            #                   [blank, left, right]
            if not root: return True

            isRightValid = validBST(root.right)
            isLeftValid = validBST(root.left)

            isValidSubTree = None

            rightGreater, leftLess = True, True

            if root.right and root.right.val <= root.val:
                rightGreater = False
            
            if root.left and root.left.val >= root.val:
                leftLess = False

            if rightGreater and leftLess: 
                isValidSubTree = True
            else:
                isValidSubTree = False

            return isValidSubTree and isRightValid and isLeftValid

        return validBST(root)