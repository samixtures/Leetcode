class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort the array
        #loop through so that some value is "a"
        #when looping: enumerate and check if 
        #the value before is the same as the current value
        #if it is then continue
        
        #in the loop do the two pointer solution for two sum II
        
        res = []
        nums.sort()
        if len(nums) < 3:
            return res
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = 0, len(nums)-1
            while l < r and l != r != i:
                if nums[l] + nums[r] + a < 0:
                    l+=1
                if nums[l] + nums[r] + a > 0:
                    r-=1
                if nums[l]+nums[r]+a == 0:
                    res.append([nums[l], nums[r], a])
                    break
                else:
                    break
        return res        