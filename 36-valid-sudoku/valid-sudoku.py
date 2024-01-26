
class Solution(object):
    def isValidSudoku(self, board):
        track=set()
        for i in range(9):
            for j in range(9):
                curr=board[i][j]
                if curr !=".":
                    rowStr = curr+" in row "+str(i)
                    colStr = curr+" in col "+str(j)
                    blockStr = curr+" in block "+str((i//3)*3)+"-"+str((j//3)*3)
                    if rowStr in track or colStr in track or blockStr in track: return False
                    track.add(rowStr)
                    track.add(colStr)
                    track.add(blockStr)
                
        return True        