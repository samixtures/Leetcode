class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removing elements of value val in place, meaning
        we remove them in the array we are given rather than creating
        a new array without the values.

        i = 0
        [3, 2, 2, 3]
         0  1.  2. 3

         if nums[i] == val
         nums.pop(i)
         2, 2, 3

         while i < len(nums):
            if nums[i] == val:
                nums.pop(i)

        iterate through each element 1 time so

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)