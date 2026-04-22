class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(row,col):
            visited[row][col]=True
            perimeter=0
            
            for r,c in directions:
                nr,nc=row+r,col+c
                if not inbound(nr,nc) or grid[nr][nc]==0:
                    perimeter+=1
                elif inbound(nr,nc) and not visited[nr][nc]:
                    perimeter+=dfs(nr,nc)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return dfs(i,j)
        return 0