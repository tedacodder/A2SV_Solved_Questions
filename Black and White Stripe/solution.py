from collections import Counter
for _ in range(int(input())):
    n,k=map(int,input().split())
    x=input()
    y=Counter(x[:k])
    ans=y["W"]
    for i in range(k,n):
        y[x[i]]+=1
        y[x[i-k]]-=1
        ans=min(ans,y["W"])
    print(ans)
        
