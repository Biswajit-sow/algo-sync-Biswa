class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        no_delete=arr[0]
        one_delete=0
        result=arr[0]
        for i in range(1,n):
            prev_one_delete=one_delete
            prev_no_delete=no_delete
            no_delete=max(no_delete+arr[i],arr[i])
            v2=0
            if prev_one_delete==float('inf'):
                v2=arr[i]
            else:
                v2=prev_one_delete+arr[i]
            one_delete=max(v2,prev_no_delete)
            result=max(result,max(no_delete,one_delete))
        return result 
