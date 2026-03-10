class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=set()
        count=0
        def dfs(node):
            visited.add(node)
            for e in rooms[node]:
                if e not in visited:
                    dfs(e)
        dfs(0)
        return len(visited)==len(rooms)

        