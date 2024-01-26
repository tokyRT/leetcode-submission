
class Solution(object):
    def isValidSudoku(self, board):
        #row by row
        for i in range(9):
            count = {str(k):0 for k in range(0,10)}
            for j in range(9):
                curr=board[i][j]
                if curr != '.': 
                    count[curr]+=1
                    if count[curr] > 1: return False
        #col by col
        for i in range(9):
            count = {str(k):0 for k in range(0,10)}
            for j in range(9):
                curr=board[j][i]
                if curr != '.': 
                    count[curr]+=1
                    if count[curr] > 1: return False
            print(count)
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
                

        return True
        