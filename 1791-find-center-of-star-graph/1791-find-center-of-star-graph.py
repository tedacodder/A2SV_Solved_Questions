class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a,b=edges[0]
        c,d=edges[1]
        if a==c or a==d:
            return a
        else:
            return b
        #convert to adjecency list
        # addlist=defaultdict(list)
        # for e in edges:
        #     u,v=e
        #     addlist[u].append(v)
        #     addlist[v].append(u)
        # for i in addlist:
        #     if len(addlist[i])==len(edges):
        #         return i
