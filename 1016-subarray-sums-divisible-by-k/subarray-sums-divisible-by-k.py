class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefix_sum=0
        res=0
        f={0:1}
        for i in range(n):
            prefix_sum+=nums[i]
            rem=prefix_sum % k
            if rem<0:
                rem=rem+k
            if rem in f:
                res+=f[rem]
            if rem in f:
                f[rem] += 1
            else:
                f[rem] = 1
        return res
