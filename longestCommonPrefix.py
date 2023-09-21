class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        standard = strs[0]

        for i in range(len(strs)):
            temp = ""
            j = 0
            while j < len(standard) and j < len(strs[i]):
                if strs[i][j] == standard[j]:
                    temp += standard[j]
                    j += 1
                else:
                    standard = temp
                    break
            standard = temp
        return standard

                

        """
        compare all characters in standard to
        strs[0] and create a new standard based on which
        characters at the begginning are the same
        then store that in temp

        then compare all characters in new standard with
        strs[1] and create a new standard basedon that

        then do the same with new standard and strs[2]
        all the way until we are done with the strs list

        we have to also make sure that when comparing lists
        we stop comparing if we reach the end one of the 
        strings or if a character in the new standard
        isn't the same as the strs[i]
        """