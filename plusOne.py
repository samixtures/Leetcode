class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        if digits[-1] == 9 and len(digits) == 1:
            digits[-1] = 1
            digits.append(0)
            return digits
        elif digits[-1] == 9 and len(digits) > 1:
            digits[-1] = 0
            backwards = -2
            while backwards >= len(digits)*-1 and digits[backwards] == 9:
                digits[backwards] = 0
                backwards -= 1
            if backwards >= len(digits)*-1:
                digits[backwards] += 1
            else:
                digits[backwards+1] = 1
                digits.append(0)
        return digits     

        """
        if digits[-1] == 9 and len(digits) > 1:
            digits[-1] = 0
            backwards = -2
            while if backwards >= len(digits)*-1 and digits[backwards] == 9:
                digits[backwards] = 0
                backwards -= 1
            digits[backwards+1] = 1
            
        """