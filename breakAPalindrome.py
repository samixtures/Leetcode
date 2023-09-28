class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        """
        Problem: if all letters are "a" excpet for 1
        then by changing tha 1 letter to "b" we create
        a palindrome

        We can determine whether this is the case or not
        by creating a frequency map and checking if 
        the value of the key "a" is exactly
        len(palindrome)-2
        if so, then we change the second occurence of "a"
        to "b"

        Did some relatively complicated tasks I didn't explain here

        Time Complexity: O(n), iterating through each character
        and using O(1) conditionals and O(1) replacements
        or creations of new variables

        Space Complexity: O(n), because of the frequency map
        """
        if len(palindrome) == 1:
            return ""

        freqMap = {}
        for x in palindrome:
            if x not in freqMap:
                freqMap[x] = 1
            else:
                freqMap[x] += 1
        if "a" in freqMap and freqMap["a"] == len(palindrome)-1:
            aCounter = 0
            for i in range(len(palindrome)):
                if palindrome[i] == "a":
                    aCounter += 1
                if aCounter == freqMap["a"]:  # finds last iteration of "a"
                    palindrome = palindrome[:i] + "b" + palindrome[i+1:]
                    return palindrome

        for x in palindrome:
            if x != "a":
                palindrome = palindrome.replace(x, "a", 1)
                return palindrome
        palindrome = palindrome[:1] + "b" + palindrome[2:]
        return palindrome
        
        # charSet = palindrome[0]
        # resultStr = ""


        # for i in range(len(palindrome)):
        #     if palindrome[i] != palindrome[0]:
        #         resultStr = palindrome[:i] + palindrome[0] + palindrome[i+1:]
        #         return resultStr
        # if charSet == 1:
        #     return ""
        # return resultStr