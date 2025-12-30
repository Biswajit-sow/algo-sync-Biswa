class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        i=1
        count=1
        store=[]
        n=len(arr)
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                count+=1
                
            else:
                store.append(count)
                count=1
        store.append(count)
        store.sort()
        for j in range(1, len(store)):
            if store[j]==store[j-1]:
                return False
        return True

        
        