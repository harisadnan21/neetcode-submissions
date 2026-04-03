class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for row in range(n):
            for col in range(n):
                if row > col:
                    #transpose
                    upper = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row] = upper
                
        for row in range(n):
            for col in range(n):
                #reflect from the middle vertically
                if col < n // 2:
                    right = matrix[row][n - col -1]
                    matrix[row][n - col -1] = matrix[row][col]
                    matrix[row][col] = right
    