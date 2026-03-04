class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        currSum = 0
        sumCount = {0: 1}  # prefix sum 0 occurs once initially

        for num in nums:
            currSum += num
            if currSum - k in sumCount:
                count += sumCount[currSum - k]
            sumCount[currSum] = sumCount.get(currSum, 0) + 1

        return count
