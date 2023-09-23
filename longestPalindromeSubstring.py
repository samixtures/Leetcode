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

    if len(str) == 1: return str[0]

    start char = 0, end char = 0 + 1
    end char goes until end

    start char = 1, end char = 1 + 1
    end char goes until end
    etc

    Time Complexity: O(n(log(n))) iterates through each character once
    and then iterates less than that for each character we iterate through

    Space Complexity: O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s[0]

        resultStr = s[0]

        for i in range(len(s)):
            if len(resultStr) > (len(s)-i):
                break
            tempStr = s[i]
            for j in range(i+1, len(s)):
                # if len(resultStr) > (j-i)+1:
                #     break
                tempStr += s[j]
                if self.isPalindrome(tempStr) and len(tempStr) > len(resultStr):
                        resultStr = tempStr 
        
        return resultStr