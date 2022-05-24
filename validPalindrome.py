class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 2 pointers
        # l = 0, r = len(s)-1
        # while l <= r
        # while s[l] and r[l] are not alphanum -> !s[l].alphanum()
        # l+=1 r+=1
        # if s[l].lower != s[r].lower: return False
        
        l, r = 0, len(s)-1
        while l<r:
            while s[l].isalnum() == False and l<r:
                l+=1
            while s[r].isalnum() == False and l<r:
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
                