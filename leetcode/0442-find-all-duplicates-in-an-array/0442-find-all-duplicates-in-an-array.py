class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                ans.append(nums[i])
        return ans

        