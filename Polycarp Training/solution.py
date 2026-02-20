#https://codeforces.com/problemset/problem/1165/B
a=int(input())

x=[int(i) for i in input().split()]
x.sort()
count=0
carry=0
i=1

for n in x:
    if n>=i:
        count+=1
        i+=1

print(count)
