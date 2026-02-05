class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        s=set(range(left,right+1))
        for i in ranges:
            s-=set(range(i[0],i[1]+1))
        return len(s)==0

        