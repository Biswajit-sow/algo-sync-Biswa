class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        len_str=len(s)
        max_length=0
        for i in range(len_str):
            seen=set()
            count=0
            for j in range(i,len_str):
                if s[j] not in seen:
                    seen.add(s[j])
                    count+=1
                else:
                    break 
            max_length=max(max_length,count)
        return max_length

        