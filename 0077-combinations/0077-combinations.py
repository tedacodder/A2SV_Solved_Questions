class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def backtrack(i=1,res=[]):
            if len(res)==k:
                ans.append(res[:])
            if len(res)>k:
                return
            for j in range(i,n+1):
                res.append(j)
                backtrack(j+1,res)
                res.pop()
        backtrack()
        return ans