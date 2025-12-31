import math
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_numbers = [pow(i, 2) for i in nums]

        squared_numbers.sort()
        return squared_numbers



        '''     
or line 4 
        squared_numbers = []

                for i in nums:
                    squared_numbers.append(pow(i, 2))'''