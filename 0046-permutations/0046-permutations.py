class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        check=[False]*len(nums)
        def perm(path=[]):
            if len(path)==len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if check[i]:
                    continue
                path.append(nums[i])
                check[i]=True
                perm(path)
                check[i]=False
                path.pop()
                
        perm()
        return ans
