class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=0
        for i in nums:
            if n!=i:
                return n
            n+=1
        return n