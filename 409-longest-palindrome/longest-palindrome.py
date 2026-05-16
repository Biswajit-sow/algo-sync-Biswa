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



'''
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
                res+=val-1# if any char is 3 freq then res+=3-1=2 so add to and 1 remain 
                bool_odd=True
        if bool_odd==False:
            return res 
        else:
            return res+1 # for odd string ----  middile 1  add 
'''

'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_freq = {}
        res = 0
        odd_found = False

        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1

        for val in s_freq.values():

            if val % 2 == 0:# for even palindrome
                res += val
            else: # for odd palindrome
                res += val - 1# if any char is 3 freq then res+=3-1=2 so add to and 1 remain 
                odd_found = True

        if odd_found:
            return res + 1

        return res
'''