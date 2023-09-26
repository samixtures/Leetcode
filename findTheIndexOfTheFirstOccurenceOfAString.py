class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        haystack and needle are string names not values

        they both have values, len(needle) <= len(haystack)

        The letters in needle need to occur in the same order
        in haystack

        Can't use frequency map or set

        Find where needles[0] occurs in haystack
        then check if len(haystack) - i < len(needle) and
        if it is then continue 

        otherwise, iterate through needle and check if every
        letter in order is the same as the letters in order of haystack
        until either we iterate all the way through needle, or 
        we find a character that's different

        If we go through and find that it's the same then return i

        otherwise move on

        for i in range(len(haystack)):
            if needle)[0] == haystack[i] and (len(haystack) - i) >= len(needle):
                tempHayStr = ""
                hayIndex = i
                needIndex = 0
                while needIndex < len(needle):
                    if needle[needIndex] != haystack[hayIndex]:
                        break
                    tempHayStr += haystack[hayIndex]
                    needIndex += 1
                    hayIndex += 1
                if tempHayStr == needle:
                    return i
        return -1
    
        Time Complexity: O(nlog(n)) worst case: we iterate through every letter
        of haystack, but sometimes we stop on that letter and check the letters
        after it to see if its a matching substring to needle

        Space Complexity: O(1) we don't use any extra containers outside of 
        variables
        """

        for i in range(len(haystack)):
            if needle[0] == haystack[i] and (len(haystack) - i) >= len(needle):
                tempHayStr = ""
                hayIndex = i
                needIndex = 0
                while needIndex < len(needle):
                    if needle[needIndex] != haystack[hayIndex]:
                        break
                    tempHayStr += haystack[hayIndex]
                    needIndex += 1
                    hayIndex += 1
                if tempHayStr == needle:
                    return i
        return -1