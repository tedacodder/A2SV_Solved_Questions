class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        checked=[False]*len(nums)
        def perm(path=[]):
            if len(path)==len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):

                if checked[i]:
                    continue
                if i>0 and not checked[i-1]  and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                checked[i]=True
                perm(path)
                checked[i]=False
                path.pop()
        perm()
        return ans