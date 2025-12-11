class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        output=[]
        closest = nums[0] + nums[1] + nums[2]# first closest initilize
        for i in range(0,n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                # update closest if this sum is nearer to target
                if abs(sum-target)< abs(closest-target):
                    closest=sum
                if sum==target:
                    return sum
                elif sum< target:
                    left+=1
                else:
                    right-=1
        return closest