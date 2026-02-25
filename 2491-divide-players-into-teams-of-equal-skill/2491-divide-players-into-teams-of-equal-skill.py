class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        a=0
        b=len(skill)-1
        c=skill[0]+skill[-1]
        ans=0
        
        while a<b:
            if c==skill[a]+skill[b]:
                
                ans+=(skill[a]*skill[b])
                a+=1
                b-=1

            else:
                return -1

            
        return ans
        