class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        ord("A") is 65, and the next letters are chronologically higher than
        65 ("B" is 66, "C" is 67 and so on, for all 26 letters)

        Therefore, we subtract 64 by ord(letter) to get the number corresponding to the
        column title, which is in letters, specifically when there is only one letter.

        The idea is we do 26 to the power of whatever position we are on, and then multiply that 
        by the asciii value of the character in that position as well.

        I had to look at the solution to get it, and I'm still not completely confident in my ability to do it.

        Time Complexity: O(n) where n is the number of characters in the columnTitle string.
        Space Complexity: O(1) since we simply use a few variables.

        Generally it's a bit of a tricky problem that requires some pattern recognition, knowledge of ascii
        and some other idea that I haven't completely grasped yet.
        """
        answer, position = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter)-64
            answer += digit * 26**position
            position += 1
        return answer