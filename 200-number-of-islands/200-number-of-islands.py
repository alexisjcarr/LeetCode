class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0: return 0
        
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        return count
                    
    def dfs(self, grid, row, col):
        dir_map = [
            [-1, 0],
            [0, 1],
            [1, 0],
            [0, -1]
        ]
        
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return
        
        if grid[row][col] == '1':
            grid[row][col] = '0'
            
            for d in dir_map:
                curr_row, curr_col = d
                self.dfs(grid, row + curr_row, col + curr_col)
        