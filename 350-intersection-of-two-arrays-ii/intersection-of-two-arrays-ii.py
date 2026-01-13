class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        n1=len(nums1)
        n2=len(nums2)
        
        for i in nums1:
            if i in nums2:
                output.append(i)
                nums2.remove(i) 
            else:
                
                continue
        return output




                