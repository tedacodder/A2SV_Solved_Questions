class RandomizedSet:

    def __init__(self):
        self.Randomset=set()
        

    def insert(self, val: int) -> bool:
        if val in self.Randomset:
            return False
        self.Randomset.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.Randomset:
            self.Randomset.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.Randomset))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()