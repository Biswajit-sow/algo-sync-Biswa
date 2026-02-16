from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                return num
            freq[num] = 1
        return -1  # Won't reach if guaranteed duplicate
