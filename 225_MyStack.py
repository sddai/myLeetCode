class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.size = 0


    def push(self, x: int) -> None:
        if self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)
        self.size += 1

    def pop(self) -> int:
        if self.q1:
            for i in range(self.size - 1):
                self.q2.append(self.q1.popleft())
            res = self.q1.popleft()
        else:
            for i in range(self.size - 1):
                self.q1.append(self.q2.popleft())
            res = self.q2.popleft()
        self.size -= 1
        return res


    def top(self) -> int:
        if self.q1:
            return self.q1[self.size - 1]
        else:
            return self.q2[self.size - 1]


    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()