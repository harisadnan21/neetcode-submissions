class Solution:

    #current = [0,1] 
    # []
    # ["0","1","1","1","0"],
    # ["0","1","0","1","0"],
    # ["1","1","0","0","0"],
    # ["0","0","0","0","0"]
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
            
                    stack.append([row,col])
                    # remove the last one
                    num = 0
                    while len(stack) != 0:
                        num +=1
                        current= stack.pop()
                        print(num)
                        print(current)
                        r, c = current[0], current[1]
                        
                        if r < 0 or r > len(grid) - 1 or c < 0 or c > len(grid[0]) -1 or grid[r][c] == "0":
                            continue
                        else:
                            
                            grid[r][c] = "0"
                            stack.append([r + 1, c])
                            stack.append([r - 1, c])
                            stack.append([r, c + 1])
                            stack.append([r, c -1])
                        
        return count