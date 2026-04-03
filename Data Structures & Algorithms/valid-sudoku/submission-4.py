class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowVal = True
        colVal = True
        boxVal = True

        currSet = set()

        def checkRow(rowNum):
            for elem in board[rowNum]:
                if elem == ".":
                    continue
                if elem in currSet:
                    return False
                else:
                    currSet.add(elem)
            return True
        
        def checkCol(colNum):
            for i in range(9):
                elem = board[i][colNum]
                if elem == ".":
                    continue
                if elem in currSet:
                    return False
                else:
                    currSet.add(elem)
            return True
        
        def checkBox(i, j):
            for row in range(3):
                for col in range(3):
                    elem = board[i + row][j + col]
                    if elem == ".":
                        continue
                    if elem in currSet:
                        return False
                    else:
                        currSet.add(elem)

            return True

        for i in range(9):
            rowVal = rowVal and checkRow(i)
            currSet.clear()
        for i in range(9):
            colVal = colVal and checkCol(i)
            currSet.clear()
        for i in range(3):
            for j in range(3):
                boxVal = boxVal and checkBox(i * 3, j * 3)
                currSet.clear()
        
        return rowVal and colVal and boxVal 
        
        
        