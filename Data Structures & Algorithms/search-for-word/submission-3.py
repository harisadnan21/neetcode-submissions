class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c , idx, visitedset):
            if idx >= len(word):
                return True
            elif r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or (r,c) in visitedset or board[r][c] != word[idx]:
                return False

            else:
                visitedset.add((r, c))
                return dfs(r + 1, c, idx+ 1, visitedset.copy()) or dfs(r -1, c, idx+ 1, visitedset.copy()) or dfs(r, c + 1, idx+ 1, visitedset.copy()) or dfs(r, c -1 , idx+ 1, visitedset.copy())




        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0, set()):
                    return True
        
        return False

        


        