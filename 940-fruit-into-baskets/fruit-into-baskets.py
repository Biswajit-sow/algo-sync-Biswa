
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        if n == 0:
            return 0
        freq = {}
        low = 0
        max_len = 0

        for high in range(n):
            # Add fruits[high] to the window
            if fruits[high] in freq:
                freq[fruits[high]] += 1
            else:
                freq[fruits[high]] = 1

            # Shrink window while more than 2 types
            while low < n and len(freq) > 2:
                freq[fruits[low]] -= 1
                if freq[fruits[low]] == 0:
                    del freq[fruits[low]]
                low += 1
            if len(freq)==2 or len(freq)==1:
                current_len = high - low + 1
                max_len = max(max_len, current_len)
        return max_len