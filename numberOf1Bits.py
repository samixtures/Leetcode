class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Check if the rightmost bit is 1 by checking what n%2 is.
        If it is then increment counter variable.
        Shift all bits to the right by one by the >> operator.
        
        All in a while loop wit the condition that n is not 0.
        I didn't understand this at first but now I get that if we shift
        0000000000000000000000000001011 to the right 2 times it's still 10
        but if we shift it 4 times its value is actually 0.
        """

        counter = 0
        while n != 0:
            if n%2 == 1:
                counter += 1
            n = n >> 1
        return counter

"""
n = 0b00000000000000000000000000001011 # if we don't ahdd the 0b it says it can't have leading zeros
print("type is", type(n)) # prints out integer
counter = 0
while n != 0:
    if n%2 == 1:
        counter += 1
    n = n >> 1
print(counter)
"""