from collections import Counter
n,m=map(int,input().split())
x=Counter([int(i) for i in input().split()])
y=Counter([int(i) for i in input().split()])

count=0
for key in x:
    if key in y:
        count+=y[key]*x[key]
print(count)


