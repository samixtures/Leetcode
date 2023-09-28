class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        words and spaces

        after every space, check how many
        characters until the next space

        length has to be at least 1

        we can just do s[-1], s[-2]
        until we reach a space 
        """
        counter = 0
        i = -1
        while s[i] == " ":
            i -= 1
        while i > (len(s)*-1)-1 and s[i] != " ":
            counter += 1
            i -= 1
        return counter