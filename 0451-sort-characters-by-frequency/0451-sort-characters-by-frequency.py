class Solution:
    def frequencySort(self, s: str) -> str:
        x=Counter(s).most_common()
        ans=[]
        for char,i in x:
            ans.append(char*i)
        return "".join(ans)
        

        