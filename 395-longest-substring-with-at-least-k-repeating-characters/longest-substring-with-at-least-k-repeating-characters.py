class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for target in range(1, 27):  # number of unique chars
            freq = {}
            left = 0
            right = 0
            unique = 0
            at_least_k = 0

            while right < n:
                # expand window
                ch = s[right]
                if ch not in freq:
                    freq[ch] = 0
                    unique += 1
                freq[ch] += 1
                if freq[ch] == k:
                    at_least_k += 1

                right += 1

                # shrink if too many unique
                while unique > target:
                    ch = s[left]
                    if freq[ch] == k:
                        at_least_k -= 1
                    freq[ch] -= 1
                    if freq[ch] == 0:
                        del freq[ch]
                        unique -= 1
                    left += 1

                # valid window
                if unique == target and at_least_k == target:
                    ans = max(ans, right - left)

        return ans
