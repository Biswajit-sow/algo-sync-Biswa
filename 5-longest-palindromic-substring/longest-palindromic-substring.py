class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        def expandAroundCenter(left: int, right: int) -> tuple:
            """Expand around center and return (start, end) indices"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindrome boundaries
            return left + 1, right - 1
        
        start, end = 0, 0
        
        for i in range(len(s)):
            # Case 1: Odd length palindrome (single character center)
            left1, right1 = expandAroundCenter(i, i)
            
            # Case 2: Even length palindrome (two character center)
            left2, right2 = expandAroundCenter(i, i + 1)
            
            # Update if we found a longer palindrome
            if right1 - left1 > end - start:
                start, end = left1, right1
            
            if right2 - left2 > end - start:
                start, end = left2, right2
        
        return s[start:end + 1]
