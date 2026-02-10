class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            if target-nums[i] in dic:
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]]=i
        






        






        # dic={}
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in dic:
        #         return [dic[complement], i]
        #     dic[num] = i
                
