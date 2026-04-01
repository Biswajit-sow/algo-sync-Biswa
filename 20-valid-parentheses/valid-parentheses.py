class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        
        for i in range(n):
            if (s[i] == '(' or s[i] == '{' or s[i] == '['):
                stack.append(s[i])
            
            else:
                # if closing bracket comes and stack is empty
                if len(stack) == 0:
                    return False
                
                if (s[i] == ')' and stack[-1] == '('):
                    stack.pop()
                elif (s[i] == '}' and stack[-1] == '{'):
                    stack.pop()
                elif (s[i] == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False   # mismatch case
        
        if len(stack) != 0:
            return False
        
        return True