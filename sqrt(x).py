class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Can be >= 0

        0 -> 0
        1 -> 1
        2 -> 1.something -> 1
        3 -> 1.something -> 1
        4 -> 2
        5 -> 2.something -> 2

        35 -> 6*6 = 36, 5*5 = 25 so 5.something -> 5

        152 -> 12*12 = 144, 13*13 = higher so 12.something -> 12

        Time Complexity: O(log(n)) where x is n
            because we'll be iterating less than n times every time
            but it's definitely not O(1)
        """
        if x == 0: return 0
        i = 0
        squared = i*i
        while squared < x:
            i += 1
            squared = i*i
            if squared == x:
                return i
        return i-1