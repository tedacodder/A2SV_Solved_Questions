class Solution:
    def binaryGap(self, n: int) -> int:
        y=str(bin(n))
        
        ans=0
        #longest distance bet
        k=0
        while k<len(y):
            if y[k]=="1":
                for i in range(k+1,len(y)):
                    if y[i]=="1":
                        ans=max(ans,i-k)
                        k=i
                        break
                else:
                    k+=1
            else:
                k+=1
        return ans
        