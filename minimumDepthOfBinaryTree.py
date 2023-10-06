# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Tree can have 0 nodes

        Iterative bfs, keep track of the levels
        """
        if not root:
            return 0
        q = [root]
        levels = 0
        while q:
            levels += 1
            for i in range(len(q)):
                currNode = q.pop(0)
                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)
                if not currNode.right and not currNode.left:
                    return levels
        return levels
            