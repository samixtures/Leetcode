# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.val == 0:
            return False
        elif root.val == 1:
            return True

        left, right = None, None
        
        if root.right.val == 3:
            if root.right.right.val == 1 and root.right.left.val == 1:
                right = True
            else:
                right = False
        elif root.right.val == 2:
            if root.right.right.val == 1 or root.right.left.val == 1:
                right = True
            else:
                right = False
        elif root.right.val == 1:
            right = True
        else:
            right = False

        if root.left.val == 3:
            if root.left.right.val == 1 and root.left.left.val == 1:
                left = True
            else:
                left = False
        elif root.left.val == 2:
            if root.left.right.val == 1 or root.left.left.val == 1:
                left = True
            else:
                left = False
        elif root.left.val == 1:
            left = True
        else:
            left = False

        print("right:", right)
        print("left:", left)

        if root.val == 2:
            return right or left
        else:
            return right and left