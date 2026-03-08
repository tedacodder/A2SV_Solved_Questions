class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        localmax=globalmax=0
        for i in range(len(nums)):
            if nums[i]==0:
                localmax=0
            else:
                localmax+=1
            globalmax=max(localmax,globalmax)
        return globalmax