class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans={}
        for s in strs:
            a=tuple(sorted(s))
            if a in ans:
                ans[a].append(s)
            else:
                ans[a]=[s]
        return list(ans.values())


        