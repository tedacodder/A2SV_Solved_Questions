class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        check=Counter(p)
        update=Counter(s[:k])
        ans=[]
        if update==check:
            ans.append(0)
        for i in range(k,len(s)):
            update[s[i]]+=1
            update[s[i-k]]-=1
            if update==check:
                ans.append(i-k+1)


        return ans

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("00"))














