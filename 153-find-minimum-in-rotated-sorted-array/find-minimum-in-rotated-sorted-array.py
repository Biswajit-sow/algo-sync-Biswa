class Solution:
    def findMin(self, nums: List[int]) -> int:
        #1st way
        #min_element=min(nums)
        #return min_element
        #2nd way
        #min_element=float("+inf")
        #for i in range(len(nums)):
            #if nums[i]<min_element:
                #min_element=nums[i]
        #return min_element
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
        