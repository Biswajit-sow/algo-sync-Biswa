class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        n1=len(nums1)
        n2=len(nums2)
        copy=nums2.copy()
        for i in nums1:
            if i in copy:
                output.append(i)
                copy.remove(i)
            else:
                
                continue
        return output




                