class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        low=0
        high=n-1
        res=-1
        if nums[0] <= nums[n-1]:
            res=nums[0]
            return res
        while(low<=high):
            guess=low+(high-low)//2
            if nums[guess]>=nums[0]:
                low=guess+1
            else:
                res=nums[guess]
                high=guess-1
        return res
        