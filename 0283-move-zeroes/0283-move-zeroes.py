class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0 #Zero
        r=0 #seeker
        while r<len(nums):
            if nums[r]!=0:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
            r+=1

        

        