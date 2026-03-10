class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited=set()
        addlist=defaultdict(list)
        for e in edges:
            u,v=e
            addlist[u].append(v)
            addlist[v].append(u)
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for i in addlist[node]:
                if i not in visited:
                    if dfs(i):
                        return True
            return False
            
        if dfs(source):
            return True
        return False


                    
        
        