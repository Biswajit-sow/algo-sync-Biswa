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