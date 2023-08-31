class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        runningSum.append(nums[0])
        temp1, temp2 = 0, 1
        for i in range(1, len(nums)):
            runningSum.append(runningSum[temp1]+nums[i])
            temp1 += 1
        return runningSum