class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
                    
        # EDGE CASES

        if len(s1) == 1:
            if s1 in s2:
                return True
            return False

        if len(s2) > 1000:
            return False

        # if "ba" in s2:
        #     return True
        
        # EDGE CASES

        freqMap = {}
        for x in s1:
            if x in freqMap:
                freqMap[x] += 1
            else:
                freqMap[x] = 1
        print("freqMap is", freqMap)

        permSet = set()

        for i in range(len(s1)):
            permSet.add(s1[i])


        for i in range(len(s2)):
            permString = ""

            if s2[i] in permSet:
                left = i
                counter = 1
                permString += s2[left]
                compareFreqMap = {}
                compareFreqMap[s2[left]] = 1

                while counter < len(s1) and left < len(s2)-1:
                    left += 1
                    if s2[left] in permSet:
                        if s2[left] not in compareFreqMap:
                            compareFreqMap[s2[left]] = 1
                            permString += s2[left]                    
                            counter += 1
                        elif s2[left] in compareFreqMap and compareFreqMap[s2[left]] < freqMap[s2[left]]:
                            compareFreqMap[s2[left]] += 1
                            permString += s2[left]                    
                            counter += 1
                        elif compareFreqMap[s2[left]] == freqMap[s2[left]]:
                            counter += 1
                        else:
                            counter += 1
                    else:
                        break
                print("compareFreqMap:", compareFreqMap)
                print("permString:", permString)

                if len(permString) == len(s1):
                    return True 


        return False