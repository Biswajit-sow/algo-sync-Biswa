class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)# len of row
        m=len(matrix[0])#len of column
        low=0
        high=n*m-1
        while(low<=high):
            guess=(low+high)//2
            row=guess//m
            col=guess%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                #move right
                low=guess+1
            else:
                high=guess-1
        return False