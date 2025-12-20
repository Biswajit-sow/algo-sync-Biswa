class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the pivot - scan RIGHT to LEFT
        # Find first position j where nums[j] < nums[j+1]
        pivot = -1
        for j in range(n-1, 0, -1):  # Changed: stop at 1, not -1
            if nums[j-1] < nums[j]:  # Changed: compare with j-1
                pivot = j-1
                break
        
        # Step 2: If no pivot found, reverse entire array
        if pivot == -1:
            nums.reverse()
            return
        
        # Step 3: Find swap element - scan RIGHT to LEFT
        # Find first position k (from right) where nums[k] > nums[pivot]
        for k in range(n-1, pivot, -1):
            if nums[k] > nums[pivot]:
                nums[pivot], nums[k] = nums[k], nums[pivot]
                break
        
        # Step 4: Reverse the right part from pivot+1 to end
        nums[pivot+1:] = reversed(nums[pivot+1:])


'''For explanation:"https://www.perplexity.ai/search/what-the-question-said-explain-_NhoV4ukRli3dCUleN9hGQ#19"'''