class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=1
        unique=1
        while(j<n):
            if nums[j]==nums[j-1]:
                j+=1
                continue
                
            
            nums[i+1]=nums[j]
            i+=1
            unique+=1
            j+=1
        return unique
        