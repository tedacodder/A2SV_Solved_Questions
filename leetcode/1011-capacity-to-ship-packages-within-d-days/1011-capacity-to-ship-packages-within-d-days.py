class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mini,maxi=max(weights),sum(weights)
        def check(minweight):
            day =0
            w=0
            for i in range(len(weights)):
                w +=weights[i]
                if w>minweight:
                    day+=1
                    w=weights[i]
            if w>0:
                day+=1
            return day<=days
        while mini<=maxi:
            mid=mini+(maxi-mini)//2
            if check(mid):
                maxi = mid - 1  # try smaller capacity
            else:
                mini = mid + 1  # need more capacity
        return mini