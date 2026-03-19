class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[]
        freq={}
        freq = Counter(nums)
        for num in freq:
            if freq[num]> n/3:
                result.append(num)
            if len(result)==2:
                break
        return result
            