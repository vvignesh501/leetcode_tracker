class MyHashMap:

    def __init__(self):
        self.myHashMap = defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.myHashMap[key] = value
        

    def get(self, key: int) -> int:
        return self.myHashMap.get(key, -1)
        

    def remove(self, key: int) -> None:
        if key in self.myHashMap:
            del self.myHashMap[key]

# Note - dict does not have a remove or put dictionary
# Use del for remove and just put dict[key] = value


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)