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
            #if unique elemenyt find then
            nums[i+1]=nums[j]
            i+=1
            unique+=1
            j+=1
        return unique



'''

def removeDuplicates(self, nums: List[int]) -> int:
    if not nums: return 0     # (Safety check for empty list)
    
    i = 0                     # Line A: The "Keeper" pointer
    
    for j in range(1, len(nums)):  # Line B: The "Scout" loop
        if nums[j] != nums[i]:     # Line C: The "New Number" check
            i += 1                 # Line D: Move Keeper forward
            nums[i] = nums[j]      # Line E: Save the new number
            
    return i + 1              # Line F: Return the count
'''
        