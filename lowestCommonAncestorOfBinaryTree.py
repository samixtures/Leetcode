# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helperLCA(root, p, q):
            if not root: return [False, False, None]

            left, right = helperLCA(root.left, p, q), helperLCA(root.right, p, q)
            
            lca = left[2] if left[2] else right[2]

            if lca:
                return [True, True, lca]

            pFound = left[0] or right[0] or root == p
            qFound = left[1] or right[1] or root == q

            print("pFound", pFound)
            print("qFound", qFound)

            if qFound and pFound:
                # if left[2] or right[2]:
                #     lca = left[2] if left[2] else right[2]
                # else:
                lca = root

            # pList = left[2] ? left[2] : right[2]
            # qList = left[3] ? left[3] : right[3]

            return [pFound, qFound, lca]

        return helperLCA(root, p, q)[2]