class Solution:
    
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        sunx=0
        for i in nums:
            if i%2==0:
                sunx+=i
        for val,i in queries:
            if nums[i]%2==0:
                sunx-=nums[i]
            nums[i]+=val
            if nums[i]%2==0:
                sunx+=nums[i]

            ans.append(sunx)
            
        return ans


        