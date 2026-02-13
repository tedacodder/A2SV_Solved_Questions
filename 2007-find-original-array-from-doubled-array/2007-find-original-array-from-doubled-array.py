class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n % 2 != 0:
            return []
        
        changed.sort()
        freq = Counter(changed)
        original = []
        
        for num in changed:
            if freq[num] == 0:
                continue
            
            if freq[2 * num] == 0:
                return []
            
            original.append(num)
            freq[num] -= 1
            freq[2 * num] -= 1
        
        return original