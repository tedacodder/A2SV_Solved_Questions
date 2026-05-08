import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for i in stones:
            heapq.heappush(heap, -i)
        while len(heap)>=2:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if x==y:
                continue
            heapq.heappush(heap,-(x-y))
        if heap:
            return -heap[0]
        return 0
        