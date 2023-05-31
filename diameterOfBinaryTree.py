# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDiamFunc(root):
            if not root: return [0, 0]

            left, right = maxDiamFunc(root.left), maxDiamFunc(root.right)

            diam = left[0] + right[0]

            length = 1 + max(left[0], right[0])

            maxDiam = max(diam, max(left[1], right[1]))

            return [length, maxDiam]

        return maxDiamFunc(root)[1]