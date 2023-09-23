class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = set()
        i = 0
        while i < len(nums):
            if nums[i] in uniqueNums:
                nums.pop(i)
            else:
                uniqueNums.add(nums[i])
                i += 1
        print(uniqueNums)
        return len(nums)