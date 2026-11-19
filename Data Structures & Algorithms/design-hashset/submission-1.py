class MyHashSet:

    def __init__(self):
        self.data = [0] * 1000001

    def add(self, key: int) -> None:
        self.data[key] = 1

    def remove(self, key: int) -> None:
        self.data[key] = 0

    def contains(self, key: int) -> bool:
        if self.data[key] == 1:
            return True
        
        return False