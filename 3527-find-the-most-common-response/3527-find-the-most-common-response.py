class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        ans=""
        x=Counter()
        maxcount=0

        for i in responses:
            for j in set(i):
                x[j]+=1
                if maxcount < x[j]:
                    maxcount=x[j]
                    ans=j
                elif x[j]==maxcount:
                    ans=min(ans,j)
        return ans
                    
        
        