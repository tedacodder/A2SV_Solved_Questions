#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1

        while right>left:
            curr=(right-left)*min(height[right],height[left])
            ans=max(ans,curr)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return ans
        



        
