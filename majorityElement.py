class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Moore Voting Algorithm:
        if there's a majority element, it will always remain in the lead
        in terms of votes (count variable) even after encountering other
        elements.

        Funny thing, it seems to only beat 82% of users in terms of memory
        (which is less than when I used the frequency map)
        but, of course, it beats 78% of users in terms of Runtime
        (which is slightly faster than the prev freq map algorithm)
        I guess they're both O(n) but my other one is like O(2n)
        """
        count, candidate = 0, None
        # candidate = nums[0]
        for x in nums:
            if count == 0:
                candidate = x
            if candidate != x:
                count -= 1
            elif candidate == x:
                count += 1
        return candidate