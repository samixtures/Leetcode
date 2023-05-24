class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # edge case: 1 pile
        if len(piles) == 1:
            if piles[0]%h == 0:
                retVal = piles[0]//h
            else:
                 retVal = piles[0]//h + 1
            # if retVal == 0:
            #     return 1
            return retVal


        left, right = 0, max(piles)
        mid = (left+right)//2

        hours = 0


        while left <= right:
            mid = (left+right)//2
            
            # to determine how many hours it will take for Koko to eat each pile
            # given banans-per-hour eating speed of mid, we must do something...
            # 
            hours = 0
            
            if mid!= 0:
                for x in piles:
                    if x%mid == 0:
                        hours += x//mid
                    else:
                        hours += x//mid + 1
            
            if hours < h:
                right = mid - 1
            elif hours > h:
                left = mid + 1
            else:
                right -= 1


        hours = 0
        if mid != 0:
            for x in piles:
                if x%mid == 0:
                    hours += x//mid
                else:
                    hours += x//mid + 1
        print("hours is", hours)

        while hours > h:
            print("we run?")
            mid += 1
            hours = 0
            if mid != 0:
                for x in piles:
                    hours += x//mid + 1
            if hours > h:
                print("we are continuing")
                print("hours is", hours)
                continue
            else:
                # mid -= 1
                break
        if mid == 0:
            return 1
        return mid