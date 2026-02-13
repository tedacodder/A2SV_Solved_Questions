class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        i=0
        j=i+1
        count=0
        while i<len(nums):
            while j<len(nums):
                if nums[i]==nums[j]:
                    if i*j%k==0:
                        count+=1
                j+=1
            i+=1
            j=i+1
        return count

        