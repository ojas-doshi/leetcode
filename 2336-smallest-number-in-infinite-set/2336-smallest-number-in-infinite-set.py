class SmallestInfiniteSet:
    
    def __init__(self):
        self.removed_set = set()

    def popSmallest(self) -> int:
        counter = 1
        while True:
            if counter not in self.removed_set:
                self.removed_set.add(counter)
                break
            counter  = counter + 1
        return counter
        

    def addBack(self, num: int) -> None:
        if num in self.removed_set: 
            self.removed_set.remove(num)
        

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)