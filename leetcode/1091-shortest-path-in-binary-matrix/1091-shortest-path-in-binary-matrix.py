class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid)
        if grid[0][0] == 1:
            return -1

        q = deque()
        q.append((0, 0, 1))   # row, col, distance

        dirs = [(-1,-1), (-1,0), (-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]


        while q:
            r, c, dist = q.popleft()

            if r==n-1 and c==n-1:
                return dist

            for dr, dc in dirs:
                nr, nc = r+dr,dc+c

                if inbound(nr,nc) and grid[nr][nc]==0:
                    grid[nr][nc]=1
                    q.append((nr,nc,dist+1))
                    

        return -1
