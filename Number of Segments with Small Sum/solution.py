#https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/C

n,s=map(int,input().split())
x=[int(i) for i in input().split()]
summ=0
ans=0
right=0
left=0
while right<len(x):
    summ+=x[right]
    while summ>s:
            summ-=x[left]
            left+=1
    ans+= (right - left + 1)
    right+=1
print(ans)
    
