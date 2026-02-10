class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        ans=[]
        for key in x:
            if x[key]>len(nums)/3:
                ans.append(key)
        return ans
        