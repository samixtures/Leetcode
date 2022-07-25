class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h = {'}':'{', ']':'[', ')':'('}
        if s[0] in h:
            return False
        stack = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                stack.append(x)
            elif len(stack)>0 and h[x] == stack[-1]:
                stack.pop(-1)
            else: return False # this is if the stack is empty AND 
                               # we run into a closed symbol. Then we DONE
        if stack:
            return False
        return True
            
            
        