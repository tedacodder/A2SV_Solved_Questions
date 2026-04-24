class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        def dfs(destination, node ,path=[0]):
            if path and node==destination:
                ans.append(path[:])
                return
            for n in graph[node]:
                path.append(n)
                dfs(destination, n ,path)
                path.pop()
        dfs(len(graph)-1,0)
        return ans



        