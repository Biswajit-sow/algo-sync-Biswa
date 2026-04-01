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

'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        matching = {
                    '(': ')',
                    '[': ']',
                    '{': '}'
                }
        for i in s :
            if i in '({[':
                stack.append(i)
            elif i in ')}]':
                if not stack:
                    return False
                top_bracket=stack.pop()
                
                current=i
                if matching[top_bracket]==current:
                    continue
                else:
                    return False
        if  not stack:
            return True
        else:
            return False
'''