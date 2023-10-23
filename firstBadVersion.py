# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        badVersions = []
        left, right = 0, n
        while left <= right:
            middle = (left + right) // 2
            # print("left:", left)
            # print("right:", right)
            # print(middle)
            if isBadVersion(middle) == True:
                badVersions.append(middle)
                # print(badVersions)
                right = middle - 1
            elif isBadVersion(middle) == False:
                left = middle + 1
        return min(badVersions)
        
        