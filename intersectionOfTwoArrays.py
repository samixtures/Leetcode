class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        I'm going to assume there is always an intersection.

        It seems like we just need to return an array
        which contains all of the values in nums1 that are in
        nums2 (or worded vice versa).

        Interesting that this question was under the "binary search"
        category. That's strange to me.


        """
        resultList = set()
        for x in nums1:
            if x in nums2:
                resultList.add(x)
        return resultList
        