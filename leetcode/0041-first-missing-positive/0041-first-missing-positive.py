class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        a=1
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
                

            if nums[i]>0 and nums[i]==a:
                a+=1
            elif nums[i]>0:
                break
        return a
        