class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    """
    currentStr += x

    if self.isPalindrome(currenStr):
        palindromeList.append(currentStr)
    1st char, 1st char + 2nd char, 1st char + 2nd char + 3rd char, etc
    2nd char, 2nd char + 3rd char, 2nd char + 3rd char + 4th char, etc
    O(n(log(n)))

    if len(str) == 1: return str[0]

    start char = 0, end char = 0 + 1
    end char goes until end

    start char = 1, end char = 1 + 1
    end char goes until end

    etc

    for i in range(len(s)):
        tempStr = s[i]
        for j in range(i+1, len(s)):
            tempStr += s[j]
            if self.isPalindrome(tempStr): palList.append(tempStr)
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s[0]

        palList = [s[0]]
        for i in range(len(s)):
            tempStr = s[i]
            for j in range(i+1, len(s)):
                tempStr += s[j]
                if self.isPalindrome(tempStr): palList.append(tempStr)
        
        resultStr = ""
        for x in palList:
            if len(x) > len(resultStr):
                resultStr = x
        return resultStr