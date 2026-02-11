class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        n1=len(t)
        if n == 0 or n1 == 0:
            return ""
        if n < n1:
            return ""
        have =[0]*256
        need= [0]*256
        for i in range(n1):
            char_index1=ord(t[i])
            need[char_index1]+=1
        
        def correct(have,need):
            for i in range(256):
                if have[i] <need[i]:
                    return False
            return True

        low = 0
        min_len = float("inf")
        current_len=0
        start=0
        for high in range(n):
            char_index=ord(s[high])
            have[char_index]+=1 
            while correct(have,need):
                current_len=high-low+1
                if current_len < min_len:
                    min_len = current_len
                    start = low
                have[ord(s[low])]-=1
                low+=1
        if min_len == float("inf"):
            return ""
        return s[start:start+min_len]
        