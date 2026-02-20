class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        x=nums[:]
        x.sort()
        for i in range(len(nums)):
            ans[i] += x.index(nums[i])
        return ans
        