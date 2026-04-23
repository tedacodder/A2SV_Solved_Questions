class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        directions=[(0,-1),(0,1),(1,0),(-1,0)]
        self.iceland=0
        def inbound(r,c):
            return 0<=r<row and 0<=c<col
        def dfs(r,c):
            grid[r][c]="0"
            for x,y in directions:
                nr,nc=r+x,c+y
                if inbound(nr,nc) and grid[nr][nc]=="1":
                    dfs(nr,nc)

        for i in range(row):
            for j in range(col):
                if grid[i][j]=="1":
                    self.iceland+=1
                    dfs(i,j)
        return self.iceland