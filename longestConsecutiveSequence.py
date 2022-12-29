class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        no binary search since unsorted so fastest is O(n)
        probably

        Since we want to check if numbers exist in constant time
        i'm thinking set

        Create a set of the list
        Loop through, use a conter var, check if 
        the current number + 1 exists in the set, if it does
        check if that number + 1 exists and so on and add to the
        counter variable as we're doing this process
        """

        # I DIDN'T CHECK FOR EDGE CASES
        # If the array is empty:
        if not nums:
            return 0
        # else:
        s = set(nums)
        counter = 1
        maxim = 1
        for x in nums:
            counter = 1
            while x + 1 in s:
                counter += 1
                x += 1
                maxim = max(counter, maxim) 
        return maxim
