class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        len(a) >= len(b)? >= 1
        
        a = "100" -> -3, -2, -1
        i = -1
        if i >= (len(a)*-1):
            if a[i] and b[i]:
                curAddition = int(a[i]) + int(b[i])
                if carryOne == True:
                    curAddition += 1
                    carryOne = False
                if curAddition == 2:
                    resultStr = "0" + resultStr
                    carryOne = True
                elif curAddition == 1:
                    resultStr = "1" + resultStr
                elif curAddition == 0:
                    resultStr = "0" + resultStr
            else: 
                resultStr = a[i] + resultStr
            i -= 1

        Time Complexity: O(n), we iterate through each
        character of the longest string one time and use
        conditionals and perform O(1) operations depending
        on those conditionals

        Space Complexity: O(1), no data structures are used,
        only variables
        """
        i = -1
        resultStr = ""
        carryOne = False
        while i >= (len(a)*-1) or i >= (len(b)*-1):
            if i >= (len(a)*-1) and i >= (len(b)*-1):
                curAddition = int(a[i]) + int(b[i])
            elif i >= (len(a)*-1):
                curAddition = int(a[i])
            elif i >= (len(b)*-1):
                curAddition = int(b[i])
            # print("currAddition", curAddition)
            if carryOne == True:
                curAddition += 1
                carryOne = False
            if curAddition == 3:
                resultStr = "1" + resultStr
                carryOne = True
            if curAddition == 2:
                resultStr = "0" + resultStr
                carryOne = True
            elif curAddition == 1:
                resultStr = "1" + resultStr
            elif curAddition == 0:
                resultStr = "0" + resultStr
            i -= 1
        if carryOne == True:
            resultStr = "1" + resultStr
        return resultStr