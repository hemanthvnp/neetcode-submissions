class Solution(object):
    def colcheck(self,col,board):
        a = {}
        for i in range(len(board)):
            if board[i][col] in a:
                return False
            else:
                if board[i][col] != '.':
                    a[board[i][col]] = 1
        return True
    def rowcheck(self,row,board):
        a = {}
        for j in range(len(board[row])):
            if board[row][j] in a:
                return False
            else:
                if board[row][j] != '.':
                    a[board[row][j]] = 1
        return True
    def matrixcheck(self,start1,start2,board):
        a = {}
        for i in range(start1,start1+3):
            for j in range(start2,start2+3):
                if board[i][j] in a:
                    return False
                else:
                    if board[i][j] != '.':
                        a[board[i][j]] = 1
        return True
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            if not self.colcheck(i,board):
                return False
            if not self.rowcheck(i,board):
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                if not self.matrixcheck(i,j,board):
                    return False
        return True
        