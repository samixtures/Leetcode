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


# NEW AND NOT COPIED? SOLUTION?
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         """
#         Edge case: if it's empty return an empty list

#         Initial thoughts:
#         sort it first
#         loop through each element in the list, and use the two
#         pointer algorithm to figure out what two other numbers
#         add with that number to make 0 as soon as possible.

#         Problem:
#         what to do when one of the pointers is equal to the index
#         of the current element we are on?
#         Hmm okay then we can add one or subtract one to the pointer
#         I guess.

#         [-1,0,1,2,-1,-4]
#         [-4,-1,-1,0,1,2]
#         """
#         nums.sort()
#         res = []
#         for x in range(len(nums)):
#             l = x+1
#             h = len(nums)-1
#             while l < h:
#                 if (nums[l] + nums[h] + nums[x]) == 0 and [nums[l], nums[h], nums[x]] not in res:
#                     res.append([nums[l], nums[h], nums[x]])
#                 elif (nums[l] + nums[h] + nums[x]) < 0:
#                     l += 1
#                 elif (nums[l] + nums[h] + nums[x]) > 0:
#                     h -= 1
#                 else:
#                     h-=1
#                     continue
#         return res
