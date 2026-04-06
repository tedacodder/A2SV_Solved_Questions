class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        x="abc"
        ans=[]
        check=[False]*3
        def backtrack(path=[]):
            if len(path)==n:
                ans.append(path[:])
                return
            for i in range(3):
                if path and path[-1]!=x[i]:
                    path.append(x[i])
                    backtrack(path)
                    path.pop()
                elif not path:
                    path.append(x[i])
                    backtrack(path)
                    path.pop()
        backtrack()
        
        if len(ans)<k:
            return ""
        return "".join(ans[k-1])