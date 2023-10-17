class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        frequency list is obviously first instinct
        but there's DEFINITELY a more memory efficient algorithm

        Apparently it peats 97% of users with Python3 in terms of memory
        """
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        maxKey, maxVal = float('-inf'), float('-inf')
        for x in freq:
            if freq[x] > maxVal:
                maxVal = freq[x]
                maxKey = x
        return maxKey