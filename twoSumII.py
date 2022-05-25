class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # check if left + right > or <
        # if it's > then move right down
        # if it's less then move left up
        # if we find the target then return l+1, r+1
        
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -=1
            if numbers[l] + numbers[r] < target:
                l +=1
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
                