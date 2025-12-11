class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        output=[]
        for i in range(0,n):
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left < right:
                sum=nums[i]+nums[left]+nums[right]
                if sum==0:
                    triplet = [nums[i], nums[left], nums[right]]
                    output.append(triplet)
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif sum<0:
                    left+=1
                else:
                    right-=1
        return output


'''Sort nums, prepare output.

For each i from 0 to n-1:

If i > 0 and nums[i] == nums[i-1], skip this i (continue).

Set left = i + 1, right = n - 1.

While left < right:

Compute sum = nums[i] + nums[left] + nums[right].

If sum == 0:

Append [nums[i], nums[left], nums[right]] to output.

Move left right, skipping duplicates.

Move right left, skipping duplicates.

Else if sum < 0: move left right.

Else: move right left.

Return output.'''