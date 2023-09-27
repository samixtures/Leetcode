class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        loop through and return index
        where the value is found

        while doing so we need to find where it might fit

        so with target 2

        we would put it between 1 and 3

        we foudn those two numbers by finding where
        the value before is lower
        and the value after is higher

        we can check for both of those conditions 
        as long as we aren't on the very first index or the 
        very last index and the length of the 
        array is greater than 2?

        well what if we're at the beggining?
        then if the number we're on is lower
        and the number after is higher
        we should return the index of the number higher,
        that's where the target belongs
        okay and that's only if the array size is at least 2

        we can actually use that same condition after
        the beggining as well
        if the current number is lower and the number after
        is higher

        we can keep doing that until we get to the last value
        then we can say if the current number is lower
        but if the current index is == len(nums)-1
        
        then we just retur the current index + 1

        actually even beforehand we return current index + 1

        Since len(nums) >= 1 we don't have to create a 
        condition fo when nums is empty

        Forgot to check if nums[i] > target:
        return 0

        Time Complexity: O(n), we just iterate through
        nums' values. Worst case we iterate through
        all of the elements. Best case we only check
        the first element.
        And then we just do a bunch of conditionals
        which are all take O(1) time

        Space Complexity: O(1) we don't use any space,
        not evenvariables I think, unless we're counting i.
        Either way O(1) time since no data structures
        are used.
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[0] > target:
                return 0
            if i == len(nums)-1 and nums[i] < target:
                return i + 1
            if nums[i] < target and nums[i+1] > target:
                return i + 1
        