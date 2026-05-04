class Solution:
    def firstUniqChar(self, s: str) -> int:
        n=len(s)
        freq={}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        '''
        for i  in range(n):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1 
        '''
                
        for i in range(n):
            if freq[s[i]]==1:
                return i
                break
            
        return -1
        