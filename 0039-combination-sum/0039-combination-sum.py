class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]

        def backtrack(path=[],sum_=0,index=0):
            if sum_==target:
                ans.append(path[:])
                return
            if sum_>target:
                return

            for i in range(index,len(candidates)):
                path.append(candidates[i])
                backtrack(path,sum_+candidates[i],i)
                path.pop()
        backtrack()
        return ans
                
        