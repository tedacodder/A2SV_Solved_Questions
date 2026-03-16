class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sums=0
        li=[]
        for a,b in costs:
            sums+=a
            li.append(b-a)
        li.sort()
        ans=sums+sum(li[:len(costs)//2:])
        return ans
        