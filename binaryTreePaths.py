# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root.left and not root.right:
            return [str(root.val)]

        leafList = [root.val]
        def helper(root):
            if not root:
                return
            leafList.append(root.val)
            helper(root.left)
            helper(root.right)
            return
        helper(root.left)
        leftLeafList = leafList
        leafList = [root.val]
        helper(root.right)
        rightLeafList = leafList
        leafList = []

        if len(leftLeafList) > 1:
            leafString = ""
            for i in range(len(leftLeafList)):
                leafString += str(leftLeafList[i])
                if i < len(leftLeafList)-1:
                    leafString += "->"

            leafList.append(leafString)

        if len(rightLeafList) > 1:
            leafString = ""
            for i in range(len(rightLeafList)):
                leafString += str(rightLeafList[i])
                if i < len(rightLeafList)-1:
                    leafString += "->"
            
            leafList.append(leafString)
                
        return leafList
        