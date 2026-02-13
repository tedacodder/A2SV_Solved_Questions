class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic={}
        ans=[]
        minindex=-1
        for i in range(len(list1)):
            if list1[i] in list2:
                val=i+list2.index(list1[i])
                dic[list1[i]]=val
                if minindex==-1:
                    minindex=val
                minindex=min(val,minindex)
        for key in dic:
            if dic[key]==minindex:
                ans.append(key)
        return ans

        

        