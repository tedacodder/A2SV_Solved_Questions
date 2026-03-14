import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    casinos = []
    for _ in range(n):
        l, r, real = map(int, input().split())
        casinos.append((l, r, real))
    
    casinos.sort()
    
    q = deque([k])
    ans = k
    i = 0
    
    while q:
        x = q.popleft()
        
        while i < n and casinos[i][0] <= x:
            l, r, real = casinos[i]
            
            if x <= r:
                q.append(real)
                ans = max(ans, real)
            
            i += 1
    
    print(ans)
