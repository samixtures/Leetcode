class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # [1, 2, 3, 4]
        # [24, 12, 8, 6]
        # loop
        # 1:value -> 1
        # 2 -> 1:value -> 1*2 and 2:value -> 1
        # 3 

        #  0  1  2  3
        # [24, 12, 8, 6]
        prod = 1
        res = []
        zero_exist = False
        zero_counter = 0
        for x in nums:
            if x != 0:
                prod*=x
            else:
                zero_exist = True
                zero_counter += 1
        for x in nums:
            if zero_counter > 1:
                res.append(0)
            elif zero_exist == True:
                if x != 0:
                    res.append(0)
                else:
                    res.append(int(prod))
            else:
                if x != 0:
                    res.append(int(prod/x))
        return res