class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        prefix_sum=0
        res=0
        f={}
        zero=0
        one=0
        for i in range(n):
            if (nums[i]==0):
                zero+=1
            else:
                one+=1
            diff= zero-one
            if (diff==0):
                res=max(res,i+1)
                continue
            if diff  not in f :# not in hashmap and add it in hashmap 
                f[diff]=i
            else:
                
                length=i-f[diff]
                res=max(length,res)
        return res

         