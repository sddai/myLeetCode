class RandomizedSet:

    def __init__(self):
        self.valToIndex = dict()
        self.arr = []
        self.size = 0


    def insert(self, val: int) -> bool:
        # print("in insert: ", self.valToIndex)
        if val not in self.valToIndex:
            self.arr.append(val)
            self.size += 1
            self.valToIndex[val] = self.size - 1
            return True
        else:
            return False


    def remove(self, val: int) -> bool:
        
        if val in self.valToIndex:
            idx = self.valToIndex[val]
            lastval = self.arr[self.size - 1]
            self.arr[idx], self.arr[self.size - 1] = self.arr[self.size - 1], self.arr[idx]
            # self.valToIndex[val], self.valToIndex[self.arr[self.size - 1]] = self.valToIndex[self.arr[self.size - 1]], self.valToIndex[val]
            self.arr.pop()
            self.size -= 1
            # self.valToIndex.pop(val)
            # del self.valToIndex[val]
            self.valToIndex[lastval] = idx    # 发现只有一个0的时候remove之后dict里边还剩下一个0，这是由于，del掉val之后又添加了lastval，当二者一样的时候，就又一次添加回来了。所以del应该放在最后
            # print("in remove: ", self.valToIndex)
            del self.valToIndex[val]
            return True
        else:
            return False
            

    def getRandom(self) -> int:
        # print(self.valToIndex)
        return self.arr[random.randint(0, self.size - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()