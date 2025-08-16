# 二叉堆
class SeatManager:

    def __init__(self, n: int):
        self.seats = [i + 1 for i in range(n)]
        self.n = n

    
    def sink(self, root):   # 大的下沉
        q = self.seats
        n = self.n
        left = root * 2 + 1
        right = root * 2 + 2
        min_index = root
        if left < n and q[left] < q[min_index]:
            min_index = left
        if right < n and q[right] < q[min_index]:
            min_index = right
        if min_index != root:
            q[min_index], q[root] = q[root], q[min_index]
            self.sink(min_index)
    
    def swim(self, i):
        parent = (i - 1) // 2
        if parent < 0:
            return 
        q = self.seats
        # if q[parent] < q[i]:
        if q[parent] > q[i]:  # 小顶堆，小的上浮
            q[parent], q[i] = q[i], q[parent]
            self.swim(parent)

    def add_item(self, item):
        q = self.seats
        self.n += 1
        n = self.n
        q[n - 1] = item
        self.swim(n - 1)
    

    def pop_min(self):
        n = self.n
        q = self.seats
        res = q[0]
        q[0], q[n - 1] = q[n - 1], q[0]
        self.n -= 1
        self.sink(0)
        return res


    def reserve(self) -> int:
        # return heapq.heappop(self.seats)  # 自己实现一个
        return self.pop_min()

    def unreserve(self, seatNumber: int) -> None:
        # heapq.heappush(self.seats, seatNumber)  # 自己实现一个
        self.add_item(seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)