class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        freq={}
        for i in  arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        #freq={1: 2, 2: 3}
        freq_counts=freq.values() #freq_counts={2,3}
        if len(set(freq_counts))==len(freq_counts):
            return True
        return False






'''
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
'''
        
        