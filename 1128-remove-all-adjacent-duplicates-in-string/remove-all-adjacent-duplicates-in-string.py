class Solution:
    def removeDuplicates(self, s: str) -> str:
        n=len(s)
        char_stack = []
        res=[]
        for i in range(n):
            if len(char_stack) == 0:
                char_stack.append(s[i])
            else:
                if char_stack[-1] == s[i]:
                    char_stack.pop()
                else:
                    char_stack.append(s[i])

        while len(char_stack)!=0:
            res.append(char_stack[-1])
            char_stack.pop()
        res.reverse()
        return "".join(res)
