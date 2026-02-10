class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            num=[]
            while i>9:
                num.append(i%10)
                i=i//10
            num.append(i)
            num.reverse()
            ans.extend(num)
        return ans
