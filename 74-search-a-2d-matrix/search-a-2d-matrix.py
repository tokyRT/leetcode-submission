def getRow(i, lenRow):
    return i//lenRow
class Solution(object):
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        row=0
        col=len(matrix[0])-1
        while row < n and col > -1:
            curr = matrix[row][col]
            if target == curr: return True
            elif target > curr: row+=1
            else: col-=1
        return False
        