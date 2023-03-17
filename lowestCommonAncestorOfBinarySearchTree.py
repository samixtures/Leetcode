# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5, null, null, null, null]
        #. 1. 2. 2. 3. 3. 3. 3  4.    4.    4. 4.  4.   4.   4.      4
        # 0 and 4's parent is 2
        # 7 and 9

        rootRef1 = root
        pAncestors = []
        while rootRef1.val != p:
            pAncestors.append(rootRef1.val)
            if p < rootRef1.val:
                rootRef1 = rootRef1.left
            elif p > rootref1.val:
                rootReft1 = rootRef1.right
                rootRef1 = root
        rootRef2 = root
        qAncestors = []
        while rootRef2.val != q:
            qAncestors.append(rootRef2.val)
            if q < rootRef2.val:
                rootRef2 = rootRef2.left
            elif q > rootref2.val:
                rootReft2 = rootRef2.right