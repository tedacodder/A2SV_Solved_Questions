class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        store=defaultdict(list)
        count=0
        for i in range(len(nums)):
            for j in store[nums[i]]:
                if i*j%k==0:
                    count+=1
            store[nums[i]].append(i)
        return count

        
        # count=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]==nums[j] and i*j%k==0:
        #             count+=1
        # return count

        