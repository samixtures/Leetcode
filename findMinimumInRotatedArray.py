class solution:
    def findMin(self, nums) -> int:
        """
        specific type of binary search

        0 1 2 3 4 5 6
        4 5 6 7 0 1 2
        l     m     r

        6+0//2 == 3

        curMin = nums[m]
        if nums[m] >= nums[l]:
            then we eleminate the left half which is weird because you'd think if you found a lower value then
            you'd want to have that value as the minimum and chec it's side rather than eliminate that side.
            Well we can make it the minimum then eliminate its side?
            curMin = min[nums[m], nums[l]]
            l = m + 1

            Let's just make sure that if the left is smaller than the right the minimum for sure can't be in the middle
            of m and l. Well I guess since it was ascending at one point, if l < m then everything in between
            is either greater than or equal to l right. Okay that's fair so we save l as the min and move to the right side
        else:
            if nums[l] > nums[m] meaning the rotation lead to a larger value before the middle value,
            then we eliminate the right, because either the middle is now the minimum or the minimum is on the left
            side because if the far left value is larger than the middle then due to the nature of a rotation
            the minimum comes after the very largest value, and we know the very largest value is somewhere on the left
            since the middle is smaller than the left now
            r = m - 1



        """
        l, r = 0, len(nums)-1
        curMin = None
        while l < r:
            m = (l+r)//2
            if nums[l] <= nums[m]:
                curMin = min(nums[l], nums[m])


with open('in.txt') as file:
    for line in file:
        intList = [int(s) for s in line.split(" ")]
        sol = solution().findMin(intList)
        print(sol)



# import os

# # Get all environment variables
# env_vars = os.environ

# # Print all environment variables and their values
# for key, value in env_vars.items():
#     print(f"{key}={value}")