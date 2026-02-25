class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum=sum(nums[:k])
        maxi=windowSum
        for i in range(k,len(nums)):
            windowSum+=nums[i]-nums[i-k]
            maxi=max(maxi,windowSum)
        return maxi/k
        