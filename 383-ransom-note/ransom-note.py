class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        m=len(ransomNote)
        magazine = list(magazine)   # convert to list so we can remove
        
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
                    