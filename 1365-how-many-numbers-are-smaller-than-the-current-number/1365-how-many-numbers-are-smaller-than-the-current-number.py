class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0]*101
        
        for num in nums:
            count[num]+=1
        
        for i in range(1,101):
            count[i]+=count[i-1]
        
        ans=[]
        for num in nums:
            if num==0:
                ans.append(0)
            else:
                ans.append(count[num-1])
        
        return ans
