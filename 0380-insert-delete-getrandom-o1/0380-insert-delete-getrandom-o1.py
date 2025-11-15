import random

class RandomizedSet:

    def __init__(self):
        self.randomMap = dict()
        self.randomList = list()

    def insert(self, val: int) -> bool:

        if val in self.randomMap:
            return False

        self.randomMap[val] = len(self.randomList)
        self.randomList.append(val)
        return True

    def remove(self, val: int) -> bool:

        if val not in self.randomMap:
            return False
        
        index = self.randomMap[val]
        last_key = self.randomList[-1]
        self.randomMap[last_key] = index
        del self.randomMap[val]
        self.randomList[index] = self.randomList[-1]
        self.randomList.pop()
        return True

    def getRandom(self) -> int:
        # Ramdom number is chosen only in a list, not in a hashset or hashmap.
        # Use list to get the random value and then remove the value in O(1) time
        return random.choice(self.randomList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()