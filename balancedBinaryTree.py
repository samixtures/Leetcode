# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root: return [0, True]

            left, right = helper(root.left), helper(root.right)

            currentlyBalanced = False

            if abs(left[0] - right[0]) <= 1 and left[1] and right[1]:
                currentlyBalanced = True

             
            return [1+max(left[0], right[0]), currentlyBalanced]

            
        return helper(root)[1]