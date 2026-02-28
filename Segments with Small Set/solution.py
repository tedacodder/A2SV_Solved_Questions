n,k=map(int,input().split())
x=[int(i) for i in input().split()]
left=0
ans=0

check=set()
for right in range(len(x)):
    if x[right] in check:
        while x[right] in check:
            check.remove(x[left])
            left+=1
    check.add(x[right])
    ans+=(len(check))
print(ans)
        
