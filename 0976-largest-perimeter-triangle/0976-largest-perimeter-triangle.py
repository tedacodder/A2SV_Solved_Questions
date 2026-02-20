class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        b=1
        ans=0
        for c in range(2,len(nums)):
            if nums[a]+nums[b]>nums[c] and nums[a]+nums[c]>nums[b] and nums[b]+nums[c]>nums[a]:
                ans=max(nums[a]+nums[b]+nums[c],ans)
            a+=1
            b+=1
        return ans