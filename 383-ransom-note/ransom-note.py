class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        i = 0   # pointer for ransomNote
        j = 0   # pointer for magazine

        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
                j += 1
            elif ransomNote[i] > magazine[j]:
                j += 1
            else:
                i+=1
                return False

        return i == len(ransomNote)