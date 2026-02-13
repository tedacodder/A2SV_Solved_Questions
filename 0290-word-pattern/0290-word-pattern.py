class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        checker={}
        checker2={}
        s=s.split()
        i=0
        
        while i<len(s) and i<len(pattern):
            if pattern[i] in checker and checker[pattern[i]]!=s[i] or s[i] in checker2 and checker2[s[i]]!=pattern[i]:
                return False
                
            else:
                checker[pattern[i]]=s[i]
                checker2[s[i]]=pattern[i]
            i+=1
        if i<len(s) or i<len(pattern):
            return False

        return True

        