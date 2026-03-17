class Solution:
    def countGoodNumbers(self, n: int) -> int:
       


        if n%2==0:
            return (pow(5,n//2,1000000007)*pow(4,n//2,1000000007))%(1000000007)
        else:
            return (pow(5,(n+1)//2,1000000007)*pow(4,(n//2),1000000007)%(10**9+7))
        # dec={0:4,1:5}
        # def count(n):
        #     if n==1:
        #         return 5
        #     return dec[n%2]*count(n-1)
        # return count(n)%(10**9+7)