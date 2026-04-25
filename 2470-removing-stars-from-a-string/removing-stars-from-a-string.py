class Solution:
    def removeStars(self, s: str) -> str:
        n=len(s)
        char_stack = []
        res=[]
       
        for i in s:
            if i== "*":
                if i!= char_stack[-1]:# star when chcek nonstar element
                    char_stack.pop() 
            else:
                char_stack.append(i)
        return ''.join(char_stack)

        