class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """

        """
        charSet = palindrome[0]
        resultStr = ""


        for i in range(len(palindrome)):
            if palindrome[i] != palindrome[0]:
                resultStr = palindrome[:i] + palindrome[0] + palindrome[i+1:]
                return resultStr
        if charSet == 1:
            return ""
        return resultStr