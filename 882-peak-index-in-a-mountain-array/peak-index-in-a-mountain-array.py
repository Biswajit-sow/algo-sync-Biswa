class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        max_index = arr.index(max(arr))
        return max_index
        