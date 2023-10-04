# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        What I failed to understand from this recurisve solution
        was how exactly nums is going to keep changing.

        I still don't understand how my iterative approach was incorrect
        but I'll have to move on from now.

        Time Complexity: O(n)? Recursion tends to be O(n) I think

        Space complexity: O(1), no data structures were really used
        outside of the given "nums"
        """
        n = len(nums)
        
        if not n:
            return None
        
        mid = (n-1)//2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root