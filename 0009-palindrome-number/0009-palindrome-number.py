class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=str(x)
        
        return y[::-1]==y
        
        