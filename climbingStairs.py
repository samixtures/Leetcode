class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Some recurrence relation top-down dynamic programming stuff here.
        
        Time Complexity: O(n)
        Space Complexity: O(n)

        Kind of complicated. I'm not very good at identifying when and how
        to use recursion and I haven't looked into dynamic programming much.
        """
        def climb(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = climb(n-1) + climb(n-2)
                return memo[n]
        memo = {1:1, 2:2}
        return climb(n)