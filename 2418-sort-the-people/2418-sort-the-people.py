class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        x=[0]*(max(heights)+1)
        y=defaultdict(list)
        k=0
        for i in range(len(heights)):
            x[heights[i]]+=1
            y[heights[i]].append(names[i])
        for height in range(len(x)-1,0,-1):
            if x[height]>0:
                for j in range(x[height]):#check
                    names[k]=y[height][j]
                    k+=1
        return names
