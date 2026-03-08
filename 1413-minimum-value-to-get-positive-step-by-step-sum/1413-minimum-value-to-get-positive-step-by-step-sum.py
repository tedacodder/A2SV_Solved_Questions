class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix=[]
        for i in nums:
            if prefix:
                prefix.append(prefix[-1]+i)
            else:
                prefix.append(i)
        mini= min(prefix)
       
        return max(1,1-mini)