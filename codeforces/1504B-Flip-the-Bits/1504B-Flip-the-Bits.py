t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    
    good = [False]*n
    ones = zeros = 0
    
    for i in range(n):
        if a[i] == '1':
            ones += 1
        else:
            zeros += 1
        if ones == zeros:
            good[i] = True
    
    flip = 0
    possible = True
    
    for i in range(n-1, -1, -1):
        cur = a[i]
        
        if flip:
            cur = '1' if cur == '0' else '0'
        
        if cur == b[i]:
            continue
        
        if not good[i]:
            possible = False
            break
        
        flip ^= 1
    
    print("YES" if possible else "NO")