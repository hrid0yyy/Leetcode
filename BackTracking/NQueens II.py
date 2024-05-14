class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isSafe(board,row,col):
            diagonalRow = 0
            diagonalCol = 0
            rup = row 
            cup = col
            rlow = row
            clow = col
            if(row>=col):
                diagonalRow = row - col
                diagonalCol = 0
            else:
                diagonalCol = col - row
                diagonalRow = 0
                
            for i in range(len(board)):
                #col check
                if(board[row][i]=="Q"):
                    return False
                # primary diagonal
                if(diagonalRow<len(board) and diagonalCol<len(board)):
                    if(board[diagonalRow][diagonalCol]=="Q"):
                        return False
                    diagonalRow += 1
                    diagonalCol += 1
                # secondary diagonal upper
                if(rup>=0 and cup< len(board)):
                    if(board[rup][cup]=="Q"):
                        return False
                    rup -= 1
                    cup += 1
                # secondary diagonal lower
                if(rlow < len(board) and clow >=0):
                    if(board[rlow][clow]=="Q"):
                        return False
                    rlow += 1
                    clow -= 1

            return True

        def helper(board,col):
            if(col==len(board)):
                allBoard.append(board)
                return 
            # putting queen row wise  
            for row in range(len(board)):
                if(isSafe(board,row,col)):
                    board[row][col] = "Q"
                    helper(board,col+1)
                    board[row][col] = "."

     
            

        allBoard = []
        board = [["."]*n for _ in range(n)]

        helper(board,0)
        return len(allBoard)
 
obj = Solution()
print(obj.totalNQueens(4))