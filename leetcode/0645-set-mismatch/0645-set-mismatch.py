class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        occ=-1
        
        for i in range(len(nums)):
            nums[abs(nums[i])-1]=-abs(nums[abs(nums[i])-1])
            if i+1<len(nums) and abs(nums[i])==abs(nums[i+1]):
                occ=nums[i]
        ans=1
        for i in range(len(nums)):
            if nums[i]>0:
                return [abs(occ),i+1]

            