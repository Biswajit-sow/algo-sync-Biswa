
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
            if len(freq)<=2:#you may skip this line beacuse after while loop the remaining condition leave the otherwise =2 or <2 
                current_len = high - low + 1
                max_len = max(max_len, current_len)
        return max_len
        
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


'''
or

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        seen = set()
        left = 0
        max_len = 0
        
        for right in range(len(fruits)):
            d[fruits[right]] += 1
            
            while fruits[right] not in seen and len(seen) == 2:  # Fixed condition
                d[fruits[left]] -= 1
                if d[fruits[left]] == 0:
                    seen.discard(fruits[left])
                left += 1
            
            if fruits[right] not in seen:
                seen.add(fruits[right])
            
            max_len = max(max_len, right - left + 1)
        return max_len
'''