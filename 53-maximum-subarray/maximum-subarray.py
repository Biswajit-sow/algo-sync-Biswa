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
        return max_sum
# but in the above code has a bug so I use the below code

'''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = max_sum = nums[0]  # Initialize properly
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])  # Restart or extend
            max_sum = max(max_sum, current_sum)
        return max_sum
'''

#no bug now










'''https://www.perplexity.ai/search/here-is-a-problem-that-intervi-mrVCjd_QS4G63tMO176h_Q#14
https://www.perplexity.ai/search/class-solution-def-maxsubarray-8Xqq9485QSiyZ7pIUFa1WA?sm=d#0
'''
