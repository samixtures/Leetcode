class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [] # the size of it should end up being n + 1
        # n = 2 -> len(ans) == 3
        # binary of 2 is 10 or 2^0*0 + 2^1*1
        # binary of 1 is 1 or 2^0 * 1
        # binary of 0 is 0 or 2^0 * 0


        """
        to convert a decimal number to binary I think we  doooo

        10 -> 1010
        10%2 = 0
        10//2 = 5
        5%2 = 1
        5//2 = 2
        2%2 = 0
        2//2 = 1
        1%2 = 1
        1//2 = 0
        """

        # n = 2

        for i in range(n+1): #n = 2 -> i = 0, 1
            temp = i
            oneCounter = 0
            while temp != 0:
                if temp % 2 == 1:
                    oneCounter += 1
                temp = temp // 2
            ans.append(oneCounter)
        return ans

        # O(n logn) time

        # reason: n is the variable n which we're given.
        #         we go through a for loop n+1 times which leads us to 
        #         O(n) time for now. Then, through each iteration of the for
        #         loop we go through a while loop, but the while loop is not
        #         going to iterate as many times as the for loop.
        #.        in fact it will iterate proportionally less as the
        #.        value of the for loop goes higher
        #.        Take 10 -> 10//2=5//2=2//2=1//2=0
        #         Take 100->100//2=50//2=25//2=12//2=6//2=3//2=1//2=0
        #         So 10 almost did half as many iterations, but 100 did
        #         much less than half the iterations ye?