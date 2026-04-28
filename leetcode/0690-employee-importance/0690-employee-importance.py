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
        self.total=0
        visited=set()
        self.indexs=defaultdict(int)
        for i in range(len(employees)):
            ids=employees[i].id
            self.indexs[ids]=i

        def dfs(i):
            visited.add(i)
            emp=employees[self.indexs[i]]
            self.total+=emp.importance
            for i in emp.subordinates:
                if i not in visited:
                    dfs(i)
        dfs(id)
        return self.total



        