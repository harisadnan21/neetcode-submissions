class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        doublesum = 0 
        for row in range(len(grid)):
            doublesum += sum(grid[row])
        if not grid or doublesum== 0 :
            return 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append([row, col, 0])

        minute = 0
        while q:
            elem = q.pop(0)
            row = elem[0]
            col = elem[1]
            minute = elem[2]

            if row< 0 or row > len(grid) -1 or col < 0 or col > len(grid[0]) -1 or grid[row][col] == 0:
                continue
            if grid[row][col] == 1 or grid[row][col] == 2:
                grid[row][col] = 0
                q.append([row + 1, col, minute +1])
                q.append([row -1, col, minute +1])
                q.append([row, col + 1, minute +1])
                q.append([row, col - 1, minute +1])
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
                
        return minute -1




        