class Solution:
    def isgood(self,word,x):
        a=Counter(word)
        for key in a:
            if a[key]>x[key]:
                return False
        return True
               

    def countCharacters(self, words: List[str], chars: str) -> int:
        x=Counter(chars)
        ans=0
        for word in words:
            count=0
            if self.isgood(word,x):
                ans+=len(word)
        return ans

        