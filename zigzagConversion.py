class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        There's a pattern.

        Pattern for letters on the same row w/o diagonals:
        originalPattern = (numRows*2) - 2

        Pattern for the diagonal letters:
        If we are not on row 0 or row numRows-1
        then it's diagonalPattern = originalPattern - 2*currentRow
        where currentRow is not 0 or n-1

        Code:
        Ceate numRows amount of lists inside of a larger list
        Append one letter of s into each list until we get to the
        last list,
        
        """