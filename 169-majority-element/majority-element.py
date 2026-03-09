from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}  # hashmap for counts
        freq = Counter(nums)
        n=len(nums)
        # Check which element is majority
        for i in nums:
            if freq[i] > n // 2:
                return i