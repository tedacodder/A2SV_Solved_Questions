#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        x=Counter(a)
        b.sort()
        for i in b:
            if i in x:
                if x[i]==1:
                    del x[i]
                else:
                    x[i]-=1
            else:
                return False
        return True
        
       
    
    
    
    
