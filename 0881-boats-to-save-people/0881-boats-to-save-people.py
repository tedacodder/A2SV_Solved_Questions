class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #p=Counter(people)
        people.sort()
        a=0
        b=len(people)-1
        count=0
        while a<=b:
            if people[a]+people[b]>limit:
                count+=1
                b-=1
            else:
                a+=1
                b-=1
                count+=1
                
        return count