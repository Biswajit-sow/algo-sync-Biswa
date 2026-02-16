class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(x):  # Use different parameter name
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10  # Integer division
            return total
        
        slow = n
        fast = n
        
        while fast != 1:
            slow = fun(slow)     # Process slow pointer
            fast = fun(fun(fast)) # Process fast pointer twice
            
            if slow == fast and slow != 1:
                return False
        return True
