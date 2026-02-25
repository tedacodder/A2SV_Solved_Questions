class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window=set()
        left=0
        ans=0
        for i in range(len(s)):
            if s[i] in window:
                while s[i] in window:
                    window.remove(s[left])
                    left+=1
            window.add(s[i])
            
            ans=max(ans,len(window))
        return ans