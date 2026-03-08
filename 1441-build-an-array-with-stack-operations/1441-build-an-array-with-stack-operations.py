class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans=[]
        l=0
        r=1
        a=1
        while a<=target[-1]:
            if a!=target[l]:
                ans.append("Push")
                ans.append("Pop")
            else:
                ans.append("Push")
                l+=1

            a+=1
        return ans

