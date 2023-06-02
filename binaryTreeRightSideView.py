# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        resList = [root.val]

        right, left = root.right, root.left

        resRight, resLeft = [root.val], [root.val]

        if right: resRight.append(right.val)
        if left: resLeft.append(left.val)


        while right and (right.right or right.left):
            if right.right:
                right = right.right
            elif right.left:
                right = right.left
            resRight.append(right.val)


        while left and (left.right or left.left):
            if left.right:
                left = left.right
            elif left.left:
                left = left.left
            resLeft.append(left.val)

        if len(resRight) < 2:
            return resLeft

        lenLeft, lenRight = len(resLeft), len(resRight)

        while lenLeft > lenRight:
            node = resLeft.pop(lenRight)
            resRight.append(node)
            lenLeft -= 1

        
        print(resRight)
        # []finalList
        # resRight = [*set(resRight)]
        # resRight = list(resRight)
        return resRight

