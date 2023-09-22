class Solution:
    def romanToInt(self, s: str) -> int:
        """
        If s[i] >= s[i+1] we add them
        Else we subtract them
            to check for this we should add each
            numeral when we see it as long as we are not on 0th
            element, after we add it, check whether the previous
            numeral was < the current one. If it was then
            subtract it twice (cancelling its addition and truly subtracting
            from the sum)

        We can create an if statement for each numeral, or we can
        create a hash map, with each numeral as the key, and its
        corresponding value as its value.
        
        This will lead to less indentations. And if you weren't going to
        indent with the if statements, the code would like somewhat strange,
        so its essentially a nicer looking solution.

        O(7) memory, but when the memory isn't dependant on a changing
        variable we simplify it to O(1) memory I believe.

        We will be iterating through each value of the string
        once: so O(n) time complexity. One might argue we look through
        most elements twice (with the exception of the final element)
        since we look at the current element and the one before it,
        but checking the previous element during an iteration and deciding
        whether to subtract from the sum or allow it to remain untampered
        is an operation taking no more than O(1) time complexity.
        """

        result = 0
        romanNumMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s)):
            result += romanNumMap[s[i]]

            if i == 0: continue

            if romanNumMap[s[i-1]] < romanNumMap[s[i]]:
                result -= (romanNumMap[s[i-1]] * 2)

    

        return result
