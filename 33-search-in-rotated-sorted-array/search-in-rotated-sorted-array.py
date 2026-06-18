class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        res=-1
        while(low<=high):
            guess=low+(high-low)//2
            if nums[guess]>=nums[0]:
                #left part
                if target >=nums[0]:
                    #if target  is in left part
                    if nums[guess]==target:
                        return guess
                    elif nums[guess]<target:
                        low=guess+1
                    else:
                        high=guess-1
                else:#target is also in right part target <nums[0]
                    low=guess+1

            else:
                if target <nums[0]:
                    #target is also in right part
                    if nums[guess]==target:
                        return guess
                    elif nums[guess]<target:
                        low=guess+1
                    else:
                        high=guess-1
                else:# target is in left half target >=nums[0]
                    high=guess-1
        return -1
                


