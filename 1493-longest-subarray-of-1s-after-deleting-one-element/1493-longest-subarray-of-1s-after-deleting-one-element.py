class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        ans=0
        right=0
        left=0
        hasdeleted=False
        while right<len(nums):
            if nums[right]==0:
                if not hasdeleted:
                    hasdeleted=True
                else:
                    while nums[left]!=0:
                        if nums[left]==1:
                            count-=1
                        left+=1
                    left+=1
                    
            else:
                count+=1
            ans=max(count,ans)
            right+=1
        if ans==len(nums):
            return ans-1
        return ans


        