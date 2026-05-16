class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_freq={}
        res=0
        for ch in s:
            s_freq[ch]=s_freq.get(ch,0)+1
        bool_odd=False
        for i in s_freq:
            val=s_freq[i]
            if val %2==0:#for even value
                res+=val#
            else:
                bool_odd=True
        if bool_odd==False:
            return res 
        else:
            for i in s_freq:
                val=s_freq[i]
                if val%2!=0:
                    res+=val-1# if any char is 3 freq then res+=3-1=2 so add to and 1 remain 
            return res+1 # for odd string ----  middile 1  add 
            