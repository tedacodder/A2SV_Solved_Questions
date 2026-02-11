class Solution:
    def findValidPair(self, s: str) -> str:
        left=0
        right=1
        counts=Counter(s)
        
        while right <len(s):
            if s[left]!=s[right] and counts[s[left]]==int(s[left]) and counts[s[right]]==int(s[right]):
                return s[left]+s[right]
            left+=1
            right+=1
            
        return ""

        