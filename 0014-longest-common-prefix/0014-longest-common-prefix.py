class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        mini=strs[0]
        maxi=strs[-1]
        ans=""
        for i in range(min(len(mini),len(maxi))):
            if mini[i]==maxi[i]:
                ans+=mini[i]
            else:
                break
        return ans
