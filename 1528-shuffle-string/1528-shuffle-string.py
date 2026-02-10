class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        x=[i for i in s]
        print(x)
        for i in range(len(indices)):
            x[indices[i]]=s[i]
        
        return "".join(x)