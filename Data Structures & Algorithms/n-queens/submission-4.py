class Solution:
    def solveNQueens(self,n):
        res = []
        board = []
        
        # cols , diag1, diag2 are sets that track all the ones that have a queen placed in them
        # diag1 is positive, diag2 is negative
        # diag1: col + row = k , diag2 : row - col
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                # check if queen is there
                if col in cols or (col + row) in diag1 or (row - col) in diag2:
                    continue
                    #can put queen there
                row_str = ["."] * n
                row_str[col] = "Q"
                board.append(row_str)
                cols.add(col)
                diag1.add((col + row))
                diag2.add((row-col))
                backtrack(row + 1, cols, diag1, diag2)
                # try not putting a queen there
                board.pop()
                cols.remove(col)
                diag1.remove((col + row))
                diag2.remove((row-col))



        backtrack(0, set(), set(), set())
        return res