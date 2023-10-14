class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        26 * x = y
        """
        ordA = ord('A')-1
        if columnNumber < 27:
            return chr(ordA + columnNumber)
        twentySixMultiple = columnNumber // 26
        firstChar, secondChar = "", ""
        secondCharNumber = None
        if twentySixMultiple < 26*27:
            firstChar = chr(ordA + twentySixMultiple)
            secondCharNumber = columnNumber - (twentySixMultiple*twentySixMultiple)
            secondChar = chr(ordA + secondCharNumber)
        return firstChar + secondChar
