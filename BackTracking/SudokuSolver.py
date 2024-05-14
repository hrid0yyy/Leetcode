class Solution(object):

    def solveSudoku(self, board):
        def isSafe(board, Row, Col, number):
            for i in range(9):
                if(number == board[Row][i] or number == board[i][Col]):
                    return False
            n = int(Row/3)*3
            m = int(Col/3)*3
            for i in range(n,n+3):
                for j in range(m,m+3):
                    if(number == board[i][j]):
                        return False
                
            return True
        
        
        def helper(board,row,col):
            if(row == len(board)):
                return True
            nrow = 0
            ncol = 0
            if(col != len(board)-1):
                nrow = row
                ncol = col + 1
            else:
                nrow = row + 1
                ncol = 0
            if(board[row][col] != "."):
                if(helper(board,nrow,ncol)):
                    return True
            else:
                for i in range(1,10):
                    if(isSafe(board,row,col,str(i))):
                        board[row][col] = str(i)
                        if(helper(board,nrow,ncol)):
                            return True
                        else:
                            board[row][col] = "."

            return False
            
            
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        print(helper(board,0,0))
        
        return board
        


board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

solver = Solution()
print(solver.solveSudoku(board))

