class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])
        row=0
        col=cols - 1
        while row < rows and col > -1:
            curr = matrix[row][col]
            if curr == target: return True
            elif target > curr: row+=1
            else: col -= 1
        return False
        