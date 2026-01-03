class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        
        n=len(nums)
        for i in range (n):
            if nums[i]>=0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        if len(neg)==0:
            for j in range(len(pos)):
                pos[j]=pos[j]*pos[j]
            return pos
        elif len(pos)==0:
            for j in range(len(neg)):
                neg[j]=neg[j]*neg[j]
            neg.reverse()
            return neg
        m=len(pos)
        t=len(neg)
        a=0
        b=0
        res=[]
        for i in range(t):
            neg[i]=neg[i]*neg[i]
        neg=neg[::-1]     # ✅ Correct (creates new reversed list)
        for i in range(m):
            pos[i]=pos[i]*pos[i]
        while a<m and b<t:
            if pos[a]<=neg[b]:
                res.append(pos[a])
                a+=1
            else:
                res.append(neg[b])
                b+=1
        while a<m:
            res.append(pos[a])
            a+=1
        while b<t:
            res.append(neg[b])
            b+=1
        return res
        




