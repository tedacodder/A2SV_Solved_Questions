class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        middle =num//3
        if num%3!=0:
            return []
        return [middle-1,middle,middle+1]
        