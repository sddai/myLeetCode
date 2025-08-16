# （差分法）48ms，71.96
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips.sort(key = lambda x: x[2])  # 不用排序
        n = len(trips)
        diff = [0] * 1001
        # diff[0] = trips[0][1]   # 【易错】不用赋初值
        # starts = [0] * n
        # ends = [0] * n
        # for i, (_, start, end) in enumerate(trips):
        #     starts[i] = trips[i][1]
        #     ends[i] = trips[i][2]
        #     # if i >= 1: diff[i] = trips[i][]
        for i in range(n):
            diff[trips[i][1]] += trips[i][0]
            diff[trips[i][2]] -= trips[i][0]   # 这里不用diff[trips[i][2] + 1]，因为到站以后人员下车，不再占用capacity
        max_passengers = 0
        for i in range(1001):
            max_passengers += diff[i]
            if max_passengers > capacity:
                return False
        return True

# 第二次一遍通过（哈希法）56ms，37.26
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        get_in = defaultdict(list)
        get_out = defaultdict(list)
        stops = set([])
        for nums, from_, to in trips:
            get_in[from_].append(nums)
            get_out[to].append(nums)
            stops.add(from_)
            stops.add(to)
        stops = list(stops)
        stops.sort()
        for stop in stops:
            if stop in get_out:
                for n_get_out in get_out[stop]:
                    capacity += n_get_out
            if stop in get_in:
                for n_get_in in get_in[stop]:
                    capacity -= n_get_in
            if capacity < 0:
                return False
        return True

        
        # 下边这个算法是用来求不重叠区间个数的，本题需要求最大重叠区间个数（区间加减法）
        # n = len(trips)
        # trips.sort(key = lambda x: x[2])
        # bound = trips[0][2]
        # max_passengers = trips[0][0]
        # if max_passengers > capacity: return False
        # for i in range(1, n):
        #     if trips[i][1] < bound:
        #         max_passengers += trips[i][0]
        #         if max_passengers > capacity:
        #             return False
        #     else:
        #         max_passengers = trips[i][0]
        #         bound = trips[i][2]
        #         if max_passengers > capacity:
        #             return False
        # return True