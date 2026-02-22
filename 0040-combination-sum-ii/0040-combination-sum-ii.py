class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans=[]
        def comb(path=[],index=0,sum_=0):
            if sum_>target:
                return
            if sum_==target:
                ans.append(path[:])
            for i in range(index,len(candidates)):
                # Skip duplicates at same level
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                comb(path,i+1,sum_+candidates[i])
                path.pop()

        comb()
        return ans