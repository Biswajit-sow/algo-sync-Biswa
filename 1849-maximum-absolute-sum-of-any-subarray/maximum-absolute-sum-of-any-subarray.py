class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        best_ending_max=nums[0]
        best_ending_min=nums[0]
        result=nums[0]
        
        for i in range(1,n):
            best_ending_max=(max(best_ending_max+nums[i],nums[i]))
            best_ending_min=(min(best_ending_min+nums[i],nums[i]))
            result=max(result,max(abs(best_ending_min),abs(best_ending_max)))
        return abs(result)