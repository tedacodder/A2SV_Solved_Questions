class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x=Counter(nums).most_common()
        ans=[]
        for i in range(len(x)):
            if i==k:
                break
            else:
                ans.append(x[i][0])        
        return ans