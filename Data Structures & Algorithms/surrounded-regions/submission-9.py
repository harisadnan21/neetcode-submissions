class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def turnT(row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != "O":
                return
            board[row][col] = "T"
            turnT(row + 1, col)
            turnT(row -1, col)
            turnT(row, col +1)
            turnT(row, col -1)
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row == 0 or row == len(board) -1 or col == 0 or col == len(board[0])-1):
                    turnT(row,col)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] =="O":
                    board[row][col] = "X"

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] =="T":
                    board[row][col] = "O"
        




        

        
        