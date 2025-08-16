# 提高效率的trick：itertools.pairwise()
from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.seats = SortedList()
        

    def seat(self) -> int:
        # 分三种情况讨论：0号位置，中间位置，n-1号位置
        to_seat = 0
        # dist = 0
        m = len(self.seats)
        if m == 0:
            self.seats.add(0)
            return 0
        prev = 0
        dist = self.seats[0]
        if m >= 2:
            for x, y in pairwise(self.seats):
                if (y - x) // 2 > dist:
                    dist = (y - x) // 2
                    to_seat = x + (y - x) // 2
            # 超时
            # for i in range(m):
            #     # if (self.seats[i] - prev) // 2 - 1 > dist: # 注意这里用的是大于号，如果用大于等于号，就会导致相同dist，后边的座位刷新了前边的座位,会导致先落座后边的座位；另外，不需要减一，因为1和0之间的距离就是1-0=1
            #     if (self.seats[i] - prev) // 2 > dist:
            #         # dist = prev + (self.seats[i] - prev) // 2 - prev -1
            #         dist = (self.seats[i] - prev) // 2
            #         # to_seat = i # 1. to_seat是中点，不是i
            #         to_seat = prev + (self.seats[i] - prev) // 2
            #     prev = self.seats[i]
        if self.n - 1 - self.seats[-1]> dist:
            to_seat = self.n - 1
        self.seats.add(to_seat)
        return to_seat

    def leave(self, p: int) -> None:
        self.seats.remove(p)
        # pass
        

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

'''
# （参考答案）pass:
from sortedcontainers import SortedList

class ExamRoom:

    def __init__(self, n: int):
        self.sl = SortedList()  # 表示已分配的座位号（有序）
        self.n = n

    def seat(self) -> int:
        # 1. 当 sl 为空时，即还没有分配座位时，分配 0 号座位
        if not self.sl:
            self.sl.add(0)
            return 0

        # 2. 当 sl 不为空时，即已经分配了若干座位（座位号有序），那么，
        # 要么分配两端的座位（0 号座位或 n - 1 号座位），
        # 要么分配两个座位号 sl[i] 和 sl[i + 1] 之间的座位：
        #   sl[i] + (sl[i + 1] - sl[i]) // 2

        # 2.1 初始分配 idx = 0 号座位，与第一个已分配座位的距离为 diff = sl[0] - 0
        # idx: 当前分配的座位号
        # diff：记录当前分配座位号与其周围（两边）已分配座位号的最大距离
        diff, idx = self.sl[0], 0

        # 2.2 分配两个座位号 sl[i] 和 sl[i + 1] 之间的座位的情况：
        #   sl[i] + (sl[i + 1] - sl[i]) // 2
        for x, y in pairwise(self.sl):  # 把这里改成用for循环找相邻两个座位的最大值，就是官方题解
            if (y - x) // 2 > diff:
                diff = (y - x) // 2
                idx = x + (y - x) // 2

        # 2.3 分配最后一个座位号 n - 1 的情况
        if self.n - 1 - self.sl[-1] > diff:
            diff = self.n - 1 - self.sl[-1]
            idx = self.n - 1

        self.sl.add(idx)
        return idx

    def leave(self, p: int) -> None:
        self.sl.remove(p)
'''

'''class ExamRoom(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.maxseats = n 
        self.lstseats = []
        self.lstnullseats = [n]

    def seat(self):
        """
        :rtype: int
        """      
        # 计算就座后的最大空位数
        maxnullseats = max([(x - 1) >> 1 for x in self.lstnullseats[1:-1]]) if len(self.lstnullseats) > 2 else 0
        # 判断是否在0就座
        if self.lstnullseats[0] >= self.lstnullseats[-1] and self.lstnullseats[0] > maxnullseats:
            self.lstseats = [0] + self.lstseats
            self.lstnullseats[0: 1] = [0, self.lstnullseats[0] - 1]
            return 0
        # 判断是否在N-1就座
        elif self.lstnullseats[-1] > self.lstnullseats[0] and self.lstnullseats[-1] > maxnullseats + 1: 
            self.lstseats.append(self.maxseats - 1)
            self.lstnullseats[-1:] = [self.lstnullseats[-1] - 1, 0]
            return self.maxseats - 1
        # 处理在中间空位就座
        else:
            # 计算就座位置lstseats[i]
            i = min(self.lstnullseats.index(maxnullseats * 2 + 1) if maxnullseats * 2 + 1 in self.lstnullseats else self.maxseats, self.lstnullseats.index(maxnullseats * 2 + 2) if maxnullseats * 2 + 2 in self.lstnullseats else self.maxseats)
            self.lstseats = self.lstseats[: i] + [self.lstseats[i - 1] + maxnullseats + 1] + self.lstseats[i :] 
            self.lstnullseats[i : i + 1] = [maxnullseats, self.lstnullseats[i] - maxnullseats - 1]
            return self.lstseats[i]

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        i = self.lstseats.index(p)
        self.lstseats.remove(p)
        self.lstnullseats[i : i + 2] = [self.lstnullseats[i] + self.lstnullseats[i + 1] + 1]
# 思路
# （1）构造一个座位数组lstseats，记录就座位置。

# （2）维护一个空位数组lstnullseats，记录就座之间的空位数，用于辅助计算。

# （3）头尾两个位置注意特殊处理下。

# 如：lstseats = [0,4,9]时，空位数组lstnullseats = [0,3,4,0]，这样方便辅助计算预留的最大空间，同时也方便处理头尾两个座位。

# 整体代码就是处理数组切片，简洁易懂
'''

'''
# 122 / 126 个通过的测试用例
from sortedcontainers import SortedSet, SortedDict
class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.distances = SortedSet([(-1, n), ], key = lambda x: self.cal_dist(x))
        self.left_dist = SortedDict({-1: (-1, n)})
        self.right_dist = SortedDict({n: (-1, n)})
    
    def cal_dist(self, dist: (int)) -> int:
        mid = dist[0] + (dist[1] - dist[0]) // 2
        # return mid - dist[0] - 1
        if dist[0] == -1:# 要注意处理两端为空座情况下的dist的计算：0号和n-1号空座时应该计算坐在端点处的距离
            return [dist[1] - dist[0] - 1, 0]
        if  dist[1] == self.n: 
            return [(dist[1] - dist[0]) // 2 - 1, -self.n]
        return [(dist[1] - dist[0]) // 2 - 1, -mid]
    
    def add_dist(self, point: (int)):
        # 注意考虑0和n-1两个特殊情况：
        if point == (-1, 0):
            return 
        elif point == (self.n - 1, self.n):
            return 
        else:
            self.distances.add(point)
            # self.left_dist.add({point[0]: point})
            # self.right_dist.add({point[1]: point})
            self.left_dist[point[0]] = point
            self.right_dist[point[1]] = point

    def remove_dist(self, point: (int)):
        self.distances.remove(point)
        self.left_dist.pop(point[0])
        self.right_dist.pop(point[1])

    def seat(self) -> int:
        if not self.distances:
            return 0
        n = self.n
        if n == 1:
            return 0
        original = self.distances[-1]
        print(self.distances)
        print(original)
        print([self.cal_dist(x) for x in self.distances])
        if original[0] == -1:
            self.remove_dist(original)
            self.add_dist((0, original[1]))
            self.add_dist((-1, 0))
            return 0
        if original[1] == n:
            self.remove_dist(original)
            self.add_dist((original[0], n - 1))
            self.add_dist((n - 1, n))
            return n - 1
        seat_num = original[0] + (original[1] - original[0]) // 2
        self.remove_dist(original)
        self.add_dist((original[0], seat_num))
        self.add_dist((seat_num, original[1]))
        print("seated in: ", seat_num)
        print("now: ", self.distances)
        return seat_num

    def leave(self, p: int) -> None:
        if self.n == 1:
            return 
        if p == 0:
            right = self.left_dist[p]
            self.remove_dist(right)
            self.add_dist((-1, right[1]))
        elif p == self.n - 1:
            left = self.right_dist[p]
            self.remove_dist(left)
            self.add_dist((left[0], self.n))
        else:                
            print("before leave: ", self.distances)
            right = self.left_dist[p]
            left = self.right_dist[p]
            self.remove_dist(left)
            self.remove_dist(right)
            self.add_dist((left[0], right[1]))
            print("after leave: ", self.distances)



# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
'''