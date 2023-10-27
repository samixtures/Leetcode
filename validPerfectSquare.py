class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        check if mid*mid < or > or ==
        """
        low, high = 0, num
        while low <= high:
            mid = (low+high)//2
            midSquared = mid*mid
            if midSquared == num:
                return True
            if midSquared < num:
                low = mid + 1
            elif midSquared > num:
                high = mid - 1
        return False
