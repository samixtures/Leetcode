class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        """
        Alright here we go.

        We can create a list containing every possible substring of the input string.
        We can then go through every substring and create a frequency map for each substring.
        After creating a frequency map, we can determine whether the substring will be a valid maximum length of a substring by getting the value of the maximum frequented key, adding k to it, and seeing if that's greater than or equal to the length of the substring window. If it is then we can compare its length to a maxLen variable, and update the value of that variable accordingly. 

        It's easier said than done...
        I only just learned how to make a list containing every substring used nested for loops (I think I'll likely forget in a bit).
        The frequency map... I don't know how we're going to associate it with specific values of the substring list.
        I guess we don't have to, all we really have to do is take a substring, create a frequency map of it, check if the max value + k is >= the length of that substring, and if it is then compare the maxLen variable with that length, and update the variable accordingly.
        """

        substring = []
        maxLen = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring.append(s[i:j])
        for string in substring:
            frequencyMap = {}
            for y in string:
                if y not in frequencyMap:
                    frequencyMap.setdefault(y, 1)
                else:
                    frequencyMap[y] += 1
            if (max(frequencyMap.values())+k) >= len(string):
                maxLen = max(maxLen, len(string))
        return maxLen
    