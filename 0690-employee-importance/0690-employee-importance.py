"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #id importance subordinates
        adlist=defaultdict(list)
        imp=defaultdict(int)
        for i in range(len(employees)):
            imp[employees[i].id]=employees[i].importance
            for su in employees[i].subordinates:
                adlist[employees[i].id].append(su)
        ans=[]
        visited=set()
        def dfs(node):
            visited.add(node)
            ans.append(imp[node])
            for nei in adlist[node]:
                if nei not in visited:
                    dfs(nei)
        dfs(id)
        return sum(ans)
        """
        visited=set()
        index=-1
        for i in range(len(employees)):
            
            if employees[i].id==id:
                index=i
                break
        count=[]
        def dfs(node):
            visited.add(node)
            if node>len(employees):
                return 



            count.append(employees[node].importance)
            for i in employees[node].subordinates:
                index=i-1
                if index not in visited:
                    dfs(index)
            
        dfs(index)
        return sum(count)
                
        """