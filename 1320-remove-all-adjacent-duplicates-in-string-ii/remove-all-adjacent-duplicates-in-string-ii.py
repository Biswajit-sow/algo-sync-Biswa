class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        n=len(s)
        res=""
        for i in range(n):
            c=s[i]
            if stack and stack[-1][0]==c:
                stack[-1]=(c,stack[-1][1]+1)
            else:
                stack.append((c,1))
            if stack[-1][1]==k:
                stack.pop()
        for char,count in stack:
            res+=char*count
        return res