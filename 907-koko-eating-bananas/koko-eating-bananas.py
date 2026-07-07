from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def fun(a, n, speed):
            hour = 0
            for i in range(n):
                hour += a[i] // speed
                if a[i] % speed != 0:
                    hour += 1
            return hour

        a = piles
        n = len(a)

        low = 1
        high = max(a)
        res = high

        while low <= high:
            guess = (low + high) // 2
            hour = fun(a, n, guess)

            if hour > h:
                low = guess + 1
            else:
                res = guess
                high = guess - 1

        return res