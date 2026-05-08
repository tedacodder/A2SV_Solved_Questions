class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        freq=Counter(words)
        
        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))
        
        res = []
        while heap and k > 0:
            count, word = heapq.heappop(heap)
            res.append(word)
            k -= 1
        return res