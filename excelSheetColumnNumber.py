class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        can't be empty string

        if len(columnTitle) > 1:
            first guy
        """
        starterVal = ord('A') - 1
        if len(columnTitle) == 1:
            return ord(columnTitle) - starterVal
        elif len(columnTitle) == 2:
            sum = 0
            sum += (ord(columnTitle[0]) - starterVal) * 26
            sum += ord(columnTitle[1]) - starterVal
            return sum
        return 0
