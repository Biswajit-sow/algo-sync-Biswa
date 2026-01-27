class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq={}
        n=len(s)
        current_len=0
        low=0
        max_len=0  
        for high in range(n):
            if s[high] in freq:
                freq[s[high]] += 1
            else:
                freq[s[high]] = 1
            while max(freq.values())> 1:
                freq[s[low]]-=1
                if (freq[s[low]]==0):
                    del freq[s[low]]
                low+=1
            if max(freq.values())==1:
                current_len=high-low+1
                max_len=max(max_len,current_len)
        return max_len
        