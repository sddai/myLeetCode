class MedianFinder:

    def __init__(self):
        self.large_heap = []   # 较大的一半，小顶堆
        self.small_heap = []   # 较小的一半，大顶堆 
        self.large_size = 0
        self.small_size = 0
        heapq.heapify(self.large_heap)
        heapq.heapify(self.small_heap)        


    def addNum(self, num: int) -> None:
        if self.small_size - self.large_size >= 0:
            # heapq.heappush(self.small_heap, -num)
            heapq.heappush(self.small_heap, -num)
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
            self.large_size += 1
        else:
            heapq.heappush(self.large_heap, num)
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))
            self.small_size += 1


    def findMedian(self) -> float:
        small = -self.small_heap[0] if self.small_size > 0 else 0
        large = self.large_heap[0] if self.large_size > 0 else 0
        # heapq.heappush(self.small_heap, -small)
        # heapq.heappush(self.large_heap, large)
        if self.small_size == self.large_size:
            return (float)(small + large) / 2
        elif self.small_size > self.large_size:
            return small
        else:
            return large
        # else:   # 这里有三种情况，不是两种
        #     return large
         
            

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()