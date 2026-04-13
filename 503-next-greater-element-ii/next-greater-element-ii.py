class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        res = [-1] * n
        
        for i in range(n-2,-1,-1):
            stack.append(nums[i])
        for i in range(n-1,-1,-1):
            while len(stack)!=0 and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack)==0:# when you don't find while in also circular then res[i]=-1
                res[i]=-1
            else:
                res[i]=stack[-1]
            stack.append(nums[i])
        return res

        