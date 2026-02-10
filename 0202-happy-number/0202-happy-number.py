class Solution:
    def sqr(self,n:int)->int:
        x=0
        while n:
            x+=(n%10)**2
            n=n//10
        return x

    def isHappy(self, n: int) -> bool:
        n=self.sqr(n)
        x=set()
        while n>9 or n not in x:
            x.add(n)
            n=self.sqr(n)
        print(x)
        if n==1:
            return True
        return False
        