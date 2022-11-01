class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # CREATE FREQUENCY MAP OF EVERY WORD AND STORE IT IN "hash_list" list
        hash_list = []
        for y in range(len(strs)):
            hash = {}
            for x in  strs[y]:
                if x in hash:
                    hash[x] += 1
                else:
                    hash[x] = 1
            hash_list.append(hash)


        # NOW THAT WE'VE CREATED A FREQUENCY MAP OF EVERY WORD AND STORED IT IN "hash_list",
        # WE CAN CREATE A SET AND A LIST, USE A NESTED FOR LOOP TO CHECK IF EACH HASH MAP IS EQUAL TO EACH OTHER
        # IF THEY ARE EQUAL ADD THEM TO THE NEW LIST AND ADD THEIR INDICES TO THE SET, AND MAKE SURE WE NEVER CHECK
        # THOSE INDICES AGAIN BASICALLY I GUESS

        indices_set = set()
        res_list = []

        print(hash_list)


        for i in range(len(hash_list)):
            temp_list = []
            if i in indices_set:
                continue
            temp_list.append(strs[i])
            for j in range(i+1, len(hash_list)):
                if j in indices_set:
                    continue
                if hash_list[i] == hash_list[j]:
                    temp_list.append(strs[j])
                    indices_set.add(j)
            res_list.append(temp_list)
        return res_list