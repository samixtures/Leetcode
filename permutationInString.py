class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == 1:
            if s1 in s2:
                return True
            return False
        
        if len(s1) > len(s2):
            return False

        firstFreqMap = {
            "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, 
            "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
        }

        for x in s1:
            firstFreqMap[x] += 1
        
        """
        sliding window frequency map for s2
        the window should be the size of len(s1)
        """

        l, r = 0, 1
        secondFreqMap = {
            "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, 
            "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
        }
        secondFreqMap[s2[l]] = 1

        while (r-l) < len(s1):
            secondFreqMap[s2[r]] += 1
            r += 1
        # print("secondFreqMap:", secondFreqMap)
        while r < len(s2):
            if secondFreqMap == firstFreqMap:
                return True
            secondFreqMap[s2[l]] -= 1
            l += 1
            secondFreqMap[s2[r]] += 1
            r+= 1
        #     print("secondFreqMap:", secondFreqMap)

        # print("firstFreqMap:", firstFreqMap)
        # print("secondFreqMap:", secondFreqMap)

        if secondFreqMap == firstFreqMap:
            return True

        return False