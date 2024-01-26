
class Solution(object):
    def isValidSudoku(self, board):
        #row by row
        for i in range(9):
            countRow = {str(k):0 for k in range(0,10)}
            countCol = {str(k):0 for k in range(0,10)}
            for j in range(9):
                currRow=board[i][j]
                if currRow != '.': 
                    countRow[currRow]+=1
                    if countRow[currRow] > 1: return False
                currCol=board[j][i]
                if currCol != '.': 
                    countCol[currCol]+=1
                    if countCol[currCol] > 1: return False
        
        #bloc by bloc
        for bi in range(0, 9, 3):
            for bj in range(0, 9, 3):
                count = {str(k):0 for k in range(0,10)}
                for i in range(bi, bi+3):
                    for j in range(bj, bj+3):
                        curr=board[i][j]
                        if curr != '.': 
                            count[curr]+=1
                            if count[curr] > 1: return False
        return True        