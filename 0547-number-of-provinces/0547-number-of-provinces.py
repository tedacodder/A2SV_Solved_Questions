class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #convert it to the adjecency list
        
        n=len(isConnected)
        visited=[False]*n
        def dfs(city): 
            for nei in range(n):
                if isConnected[city][nei]==1 and not visited[nei]:
                    visited[nei]=True
                    dfs(nei)
        count=0    
        for i in range(len(isConnected)):
            if not visited[i]:
                visited[i]=True
                dfs(i)
                count+=1
        return count