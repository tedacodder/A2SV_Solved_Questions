class Solution:
    def isValid(self, s: str) -> bool:
        dic={"}":"{",")":"(","]":"["}
        stack=[]
        for i in range(len(s)):
            if stack and s[i] in dic and stack[-1]==dic[s[i]]:
                stack.pop()
                continue
            elif stack and s[i] in dic and stack[-1]!=dic[s[i]]:
                return False
            stack.append(s[i])
        return len(stack)==0

