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
        lowestValid = float('inf')

        hours = 0


        while left <= right:
            mid = (left+right)//2
            hours = 0
            
            if mid!= 0:
                for x in piles:
                    if x%mid == 0:
                        hours += x//mid
                    else:
                        hours += x//mid + 1
                print("hours is in 1st while", hours)
                print("mid in 1st while", mid)
            # if hours == h:
            #     break
            if hours <= h and hours > 0:
                lowestValid = min(lowestValid, mid)
            if hours <= h:
                right = mid - 1
            elif hours > h:
                left = mid + 1
            # else:
            #     right -= 1
        print("lowestValid is", lowestValid)
        print("mid is finally", mid)
        if lowestValid != float('inf'):
            mid = max(lowestValid, mid)

        # hours = 0
        # if mid != 0:
        #     for x in piles:
        #         if x%mid == 0:
        #             hours += x//mid
        #         else:
        #             hours += x//mid + 1
        # print("hours is", hours)

        # while hours > h:
        #     print("we run?")
        #     mid += 1
        #     hours = 0
        #     if mid != 0:
        #         for x in piles:
        #             hours += x//mid + 1
        #     if hours > h:
        #         print("we are continuing")
        #         print("hours is", hours)
        #         continue
        #     else:
        #         break

            # if hours <= h:
            #     right = mid - 1
            # elif hours > h:
            #     left = mid + 1
            # else:
            #     right -= 1


        # hours = 0
        # if mid != 0:
        #     for x in piles:
        #         if x%mid == 0:
        #             hours += x//mid
        #         else:
        #             hours += x//mid + 1
        print("hours is", hours)

        # while hours < h:
        #     print("we run?")
        #     mid -= 1
        #     hours = 0
        #     if mid != 0:
        #         for x in piles:
        #             hours += x//mid + 1
        #     if hours > h:
        #         print("we are continuing")
        #         print("hours is", hours)
        #         continue
        #     else:
        #         break



        if mid == 0:
            return 1

        return mid