class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        
        def Pow(base=x,ex=abs(n)):
            if ex==0:
                return 1
            elif ex%2==0:
                return Pow(base*base,ex//2)
            else:
                return base*Pow(base*base,(ex-1)//2)
        ans=Pow()
        
        return float(ans) if n>0 else 1/ans
        