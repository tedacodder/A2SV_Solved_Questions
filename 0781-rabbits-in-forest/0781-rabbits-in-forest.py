class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count=Counter(answers)
        res=0
        for x,c in count.items():
            groupSize=x+1
            group=math.ceil(c/groupSize)
            res+=groupSize*group
        return res
