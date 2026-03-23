import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        permutations_iterator = itertools.permutations(nums)
        all_permutations=[]
        for p in permutations_iterator :
            all_permutations.append(list(p))
        
        return all_permutations





