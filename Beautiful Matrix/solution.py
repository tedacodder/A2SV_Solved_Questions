x=[[int(i) for i in input().split()] for _ in range(5)]

for i in range(len(x)):
    if 1 in x[i]:
        j=x[i].index(1)
        break

ans=abs(2-i)+abs(2-j)
print(ans)
