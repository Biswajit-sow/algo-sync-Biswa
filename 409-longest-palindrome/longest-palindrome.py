class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_freq = {}
        res = 0
        odd_found = False

        for ch in s:
            s_freq[ch] = s_freq.get(ch, 0) + 1

        for val in s_freq.values():

            if val % 2 == 0:
                res += val
            else:
                res += val - 1
                odd_found = True

        if odd_found:
            return res + 1

        return res