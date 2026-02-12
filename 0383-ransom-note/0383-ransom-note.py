class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans=Counter(ransomNote)
        mag=Counter(magazine)
        ans=True

        for key in rans:
            if key in mag:
                if rans[key]>mag[key]:
                    ans=False
            else:
                ans=False
        return ans
        

        