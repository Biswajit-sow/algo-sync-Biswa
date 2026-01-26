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
