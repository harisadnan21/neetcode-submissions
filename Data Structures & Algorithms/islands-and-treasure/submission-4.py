from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col, 0))
        visited = set()
        while q:

            currElem = q.popleft()
            row, col, level = currElem[0], currElem[1], currElem[2]
            if row < 0 or col < 0 or row > len(grid) -1 or (col > len(grid[0]) -1) or ((row, col) in visited) or grid[row][col] == -1:
                continue
            
            visited.add((row, col))
            grid[row][col] = level
            q.append((row -1, col, level + 1))
            q.append((row + 1, col, level + 1))
            q.append((row, col -1, level + 1))
            q.append((row, col + 1, level + 1))

        return




        