class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumSum = 0

        for account in accounts:
            maximumSum = max(sum(account), maximumSum)
        
        return maximumSum