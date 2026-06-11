class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #max_index = arr.index(max(arr))
        #return max_index
        n=len(arr)
        low=0
        high=n-1
        res=-1
        while(low<=high):
            guess=low+(high-low)//2
            if arr[guess]<arr[guess+1]:
                low=guess+1
            else:
                res=guess
                high=guess-1
        return res
            