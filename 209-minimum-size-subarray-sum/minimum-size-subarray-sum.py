class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=0
        min_len = float("inf")
        current_len=0
        cur_sum=0
        
        while(high<n):
            cur_sum+=nums[high]
            while(cur_sum>=target):
                current_len=high-low+1
                min_len=min(min_len,current_len)
                cur_sum-=nums[low]
                low+=1
            
            high+=1
        return 0 if min_len == float("inf") else min_len


'''class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=0
        min_len = float("inf")
        current_len=0
        cur_sum=0
        
        for high in range(n):
            cur_sum+=nums[high]
            while(cur_sum>=target):
                current_len=high-low+1
                min_len=min(min_len,current_len)
                cur_sum-=nums[low]
                low+=1
            
            
        return 0 if min_len == float("inf") else min_len
        '''
        