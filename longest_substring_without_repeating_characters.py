class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # edge cases
        if not len(s):
            return 0
        if len(s) == 1:
            return 1
        
        l, r, counter, max_counter = 0, 1, 1, 1
        char_set = set(s[l])

        while r < len(s):
            print("count is ", counter)
            if s[r] not in char_set:
                char_set.add(s[r])
                counter += 1
                max_counter = max(counter, max_counter)
                r += 1
            elif s[r] in char_set:
                counter -= 1
                char_set.remove(s[l])
                l += 1
        return max_counter