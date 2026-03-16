class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        
        return self.fib(n-1)+self.fib(n-2)
"""
        memo = {}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n < 2:
                return n
            memo[n] = dfs(n-1) + dfs(n-2)
            return memo[n]
        return dfs(n)
"""