class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        amountToSubtract = 2
        while n > 1:
            n -= amountToSubtract
            amountToSubtract += 1
            count += 1
        if n == 1:
            return count + 1
        return count