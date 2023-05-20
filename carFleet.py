class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        associatedHash = {}

        for i in range(len(position)):
            associatedHash[position[i]] = speed[i]
            
        sortedPos = position
        sortedPos.sort()


        l, r = len(position)-2, len(position)-1

        while l >= 0:
            # print("sortedPos", sortedPos)
            timeToTargR = (target-sortedPos[r])/associatedHash[sortedPos[r]]
            timeToTargL = (target-sortedPos[l])/associatedHash[sortedPos[l]]
            
            # print("targR:", timeToTargR)
            # print("targL:", timeToTargL)

            if timeToTargL <= timeToTargR:
                sortedPos.pop(l)
                l-=1
                r-=1
            else:
                # sortedPos.pop(r)
                r = l
                l-=1


        return len(sortedPos)