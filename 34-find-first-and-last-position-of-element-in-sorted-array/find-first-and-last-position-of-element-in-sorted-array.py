class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def first():
            n=len(nums)
            low=0
            res=-1
            high=n-1
            
            while (low<=high):
                guess=low+(high-low)//2
                if nums[guess]< target:
                    low=guess+1
                elif nums[guess]>target:
                    high=guess-1
                else:
                    res=guess
                    high=guess-1
            return res
        def last():
            n=len(nums)
            low=0
            fast=-1
            high=n-1
            
            while (low<=high):
                guess=low+(high-low)//2
                if nums[guess]< target:
                    low=guess+1
                elif nums[guess]>target:
                    high=guess-1
                else:
                    fast=guess
                    low=guess+1
            return fast
        return [first(),last()]