# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        firstTreeTravers = []
        secondTreeTravers = []
        def inorder(root, treeList):
            if not root:
                return treeList
            inorder(root.left, treeList)
            treeList.append(root.val)
            inorder(root.right, treeList)
        firstTreeTravers = inorder(p, firstTreeTravers)
        secondTreeTravers = inorder(q, secondTreeTravers)
        print("firstTreeList is", firstTreeTravers)
        print("secondTreeList is", secondTreeTravers)
        if firstTreeTravers == secondTreeTravers:
            return True
        return False