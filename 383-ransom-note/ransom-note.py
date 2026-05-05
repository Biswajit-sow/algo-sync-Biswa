class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for r in set(ransomNote):
            if r not in magazine or ransomNote.count(r) > magazine.count(r):
                return False

        return True
        '''
        2nd way
        ransom_count = {}
        magazine_count = {}

        # count frequency of ransomNote
        for ch in ransomNote:
            if ch in ransom_count:
                ransom_count[ch] += 1
            else:
                ransom_count[ch] = 1

        # count frequency of magazine
        for ch in magazine:
            if ch in magazine_count:
                magazine_count[ch] += 1
            else:
                magazine_count[ch] = 1

        # compare frequencies
        for ch in ransom_count:
            if ch not in magazine_count or ransom_count[ch] > magazine_count[ch]:
                return False

        return True


        3rd way

        m=len(ransomNote)
        magazine = list(magazine)   # convert to list so we can remove
        n=len(magazine)
        for i in range(m):
            found = False
            for j in range(len(magazine)):
                if ransomNote[i] == magazine[j]:
                    magazine.pop(j)   # remove by index
                    found = True
                    break
            if not found:
                return False

        return True


        4th ay using two pointer 
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

        return i == len(ransomNote)'''



