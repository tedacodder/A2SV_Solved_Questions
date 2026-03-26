class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minf = float("inf")
        child = [0] * k

        def backtrack(idx):
            if idx == len(cookies):
                self.minf = min(self.minf, max(child))
                return

            # Pruning
            if max(child) >= self.minf:
                return

            for i in range(k):
                child[i] += cookies[idx]
                backtrack(idx + 1)
                child[i] -= cookies[idx]

                # Avoid duplicate states
                if child[i] == 0:
                    break

        backtrack(0)
        return self.minf