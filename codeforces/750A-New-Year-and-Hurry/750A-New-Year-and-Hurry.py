#binarysearch method
n,k=map(int,input().split())

time=240-k
def binarysearch(l=0,r=n):
    ans=0
    while l<=r:
        mid=(l+r)//2
        if 5*mid*(mid+1)//2<=time:
            ans=mid
            l=mid+1
        else:
            r=mid-1
    return ans
        
            
answer=binarysearch()
print(answer)