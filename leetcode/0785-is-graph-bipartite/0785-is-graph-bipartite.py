class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)  # -1 = uncolored

        for start in range(len(graph)):
            if color[start] != -1:
                continue

            q = deque([start])
            color[start] = 0

            while q:
                node = q.popleft()
                for nei in graph[node]:
                    if color[nei] == -1:
                        color[nei] = 1 - color[node]
                        q.append(nei)
                    elif color[nei] == color[node]:
                        return False

        return True
