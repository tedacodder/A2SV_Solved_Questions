class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        two=0
        for n in nums:
            if n==0:
                zero+=1
            elif n==1:
                one+=1
            else:
                two+=1
        i=0
        for j in range(i,i+zero):
            nums[j]=0
            i+=1
        for j in range(i,i+one):
            nums[j]=1
            i+=1
        for j in range(i,i+two):
            nums[j]=2
            i+=1