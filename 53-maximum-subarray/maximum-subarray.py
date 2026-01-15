class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = 0
        max_sum = nums[0]
        
        for i in range(n):
            current_sum += nums[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
                
            if current_sum < 0:
                current_sum = 0
            
            # REMOVED line 12: max_sum = max(max_sum, current_sum) 
            
        return max_sum
