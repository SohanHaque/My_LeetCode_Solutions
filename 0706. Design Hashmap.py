class MyHashMap:

    def __init__(self):
        self.myMap = [None]*1000001

    def put(self, key: int, value: int) -> None:
        self.myMap[key] = value

    def get(self, key: int) -> int:
        if self.myMap[key] == None:
            return -1
        else:
            return self.myMap[key]

    def remove(self, key: int) -> None:
            self.myMap[key] = None
