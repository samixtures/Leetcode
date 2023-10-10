class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        If we didn't have to use constant space I would've used a frequency map

        Linear runtime means we can only loop through once, but that seems
        impossible so it'll likely be a 2 pointer solution
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != nums[right]:
                right += 1
            elif nums[left] == nums[right]: 
                nums.pop(right)
                nums.pop(left)
                left = 0
                right = 1
        print(nums)
        return nums[left]
        # if right == len(nums) and nums[right-1] != nums[left]:
        #     return nums[left]
        # else:
        #     return nums[right]
        
        