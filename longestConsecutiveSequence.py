class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        sorted approach
        we can sort and just check the sequences easily that way
        but it's O(nlog(n)) time.
        Faster than O(n^2) doe which I think my initial solution was...
        """

        if not nums:
            return 0
        nums.sort()
        streak, maxim = 1, 1
        for x in range(1, len(nums)):
            if nums[x] != nums[x-1]:
                if nums[x] == nums[x-1]+1:
                    streak += 1
                    maxim = max(maxim, streak)
                else:
                    streak = 1
        return maxim