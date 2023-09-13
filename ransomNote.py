class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteHash = {}
        magazineHash = {}

        for x in ransomNote:
            if x not in ransomNoteHash:
                ransomNoteHash[x] = 1
            else:
                ransomNoteHash[x] += 1

        for x in magazine:
            if x not in magazineHash:
                magazineHash[x] = 1
            else:
                magazineHash[x] += 1
        
        for x in ransomNoteHash:
            if x not in magazineHash or magazineHash[x] < ransomNoteHash[x]:
                # print("ransomNoteHash:", ransomNoteHash)
                # print("magazineHash:", magazineHash)
                # print("x:", x)
                return False
        return True
    
# Time Complexity: O(3n) -> O(n)
# Space Complexity: O(2n) -> O(n)