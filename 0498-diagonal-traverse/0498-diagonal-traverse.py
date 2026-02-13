class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Step 1: Group elements by (row + col)
        for i in range(m):
            for j in range(n):
                diagonals[i + j].append(mat[i][j])
        
        result = []
        
        # Step 2: Traverse diagonals in order
        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(reversed(diagonals[d]))
            else:
                result.extend(diagonals[d])
        
        return result