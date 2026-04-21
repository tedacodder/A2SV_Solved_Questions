class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def backtrack(path=[],start=0):
            ans.append(path[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(path,i+1)
                path.pop()
        backtrack()
        return ans

