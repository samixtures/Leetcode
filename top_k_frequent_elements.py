class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a frequency map of each number
        
        hash = {}
        for x in nums:
            if x in hash:
                hash[x] += 1
            else:
                hash[x] = 1

        print(hash)
        
        # After creating the frequency map, create result list and a set, loop through k times, each time loop through the
        # frequency map and check which key has the highest value, add that key to the result list, and add the key to the set for no reason
        # if the key is in the set (or list for that matter hahaha) skip that iteration of the looping through the hash map
        # so that we find the k keys with the highest values, rather than the same key with the highest value k times

        res_list = []
        s = set()

        for i in range(k):
            max_key = 0
            max_val = 0
            for x in hash:
                if x in s:
                    continue
                if hash[x] > max_val:
                    max_key = x
                    max_val = hash[x]

            s.add(max_key)
            res_list.append(max_key)
        
        return res_list
    
        
        