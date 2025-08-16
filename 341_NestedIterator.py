# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque(nestedList)

    def next(self) -> int:
        # temp = 
        return self.queue.popleft().getInteger()
     
        
    def hasNext(self) -> bool:   # hasNext不断拆包，保证调用hasNext之后的第一个元素是integer
        while self.queue and self.queue[0].isInteger() == False:   # 用while不用if
            first = self.queue.popleft().getList()   # 如果queue中的第一个元素不是整数，就把它拆包然后一个一个append到queue的头部（注意顺序是倒叙）
            for i in range(len(first) - 1, -1, -1):
                self.queue.appendleft(first[i])
        # return self.queue is not None
        return len(self.queue) > 0
            


'''
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        # self.traverse(nestedList)   # 不能这样直接把nestedList喂给traverse，因为nestedList的类型是List，里边的类型是NestedInteger
        for node in nestedList:
            self.traverse(node)
        self.it = iter(self.res)
        # print(self.it)
    
    def next(self) -> int:
        # for i in self.it:
        #     print(i)
        # return next(self.it)
        for i in self.it:
            yield i
        
    
    def hasNext(self) -> bool:
        return hasattr(self.it, "__next__")
    
    def traverse(self, nestedList):
        if nestedList.isInteger():
        # if nestedList.isInstance(List):
            self.res.append(nestedList.getInteger())   # 直接存一份在内存里会内存溢出
        else:
            for item in nestedList.getList():
                self.traverse(item)
'''    

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())