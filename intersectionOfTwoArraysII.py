class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        We need to find every number that appears in nums1 and nums2 that's the same,
        and we must add duplicates if they a number appears the same amount of times in both
        lists.

        1. nested loops, pop indices we find an intersection

        2. frequency maps, find intersection, append the number the number of times it appears less out of both arrays

        Time vs Space

        Time is more important probably so 2.
        """
        resultList = []
        freq1, freq2 = {}, {}
        for x in nums1:
            if x not in freq1:
                freq1[x] = 1
            else:
                freq1[x] += 1

        for x in nums2:
            if x not in freq2:
                freq2[x] = 1
            else:
                freq2[x] += 1
        
        timesToAppend = None
        for x in freq1:
            if x in freq2:
                if freq1[x] < freq2[x]:
                    timesToAppend = freq1[x]
                else:
                    timesToAppend = freq2[x]
                for i in range(timesToAppend):
                    resultList.append(x)
        return resultList