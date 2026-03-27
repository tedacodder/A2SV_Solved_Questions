class Solution:
    def totalNQueens(self, n: int) -> int:
        
        ans=0
        col=[False]*n
        posDiag=[False]*(2*n-1)
        negDiag=[False]*(2*n-1)
        board=[["."]*n for _ in range(n)]
        def backtrack(i=0):
            nonlocal ans
            if i==n:
                ans+=1
                return
            

            for j in range(n):
                posD=i+j
                negD=i-j
                if not col[j] and not posDiag[posD] and not negDiag[negD]:#only wanted cells
                    col[j]=posDiag[posD]=negDiag[negD]=True
                    board[i][j]="Q"
                    backtrack(i+1)
                    col[j]=posDiag[posD]=negDiag[negD]=False
                    board[i][j]="."

                
        backtrack()
        return ans