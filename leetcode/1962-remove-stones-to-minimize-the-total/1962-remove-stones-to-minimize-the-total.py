import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # make max heap
        max_heap = [-x for x in piles]
        heapq.heapify(max_heap)
        for _ in range(k):
            x=-heapq.heappop(max_heap)
            x=x-floor(x/2)
            heapq.heappush(max_heap, -x)

        return -sum(max_heap)