n,s=map(int,input().split())
x=[int(i) for i in input().split()]
ans=0
summ=0
left=0
for right in range(len(x)):
    summ+=x[right]
    while summ>=s:
        ans+=(n-right)
        summ-=x[left]
        left+=1
print(ans)
    
    
