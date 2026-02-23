class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        best_max_ending=nums[0]
        best_min_ending=nums[0]
        best_max_ending2=nums[0]
        best_max_ans=nums[0]
        best_min_ans=nums[0]
        result=nums[0]
        total_sum=sum(nums)
        n=len(nums)
        for i in range(1,n):
            prev_best_max_ending=best_max_ending
            prev_best_min_ending=best_min_ending

            best_max_ending=max(prev_best_max_ending+nums[i],nums[i])
            best_max_ans=max(best_max_ans,best_max_ending)

            best_min_ending=min(prev_best_min_ending+nums[i],nums[i])
            best_min_ans=min(best_min_ans,best_min_ending)
        if best_max_ans < 0:
            return best_max_ans 
        best_max_ending2 = total_sum - best_min_ans
        result = max(best_max_ans, best_max_ending2,best_max_ans)
        return result
