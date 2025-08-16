# 带有函数的二分法
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.n = len(weights)
        # left = min(weights)   # 注意left和right的取值
        left = max(weights)
        # right = 500
        right = sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            day = self.getDays(mid)
            if day > days:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def getDays(self, cap):
        i = 0
        ship = 0
        day = 1  # 注意起始值
        for weight in self.weights:
            if ship + weight > cap:
                day += 1
                ship = 0
            ship += weight
        return day
        # while i < self.n:   # 注意函数的写法
        #     ship += self.weights[i]
        #     if ship <= cap:
        #         i += 1
        #     else:
        #         ship = 0
        #         day += 1
        # if ship:
        #     day += 1
        return day
        # days = 0
        # ship = 0
        # for w in self.weights:
        #     ship += w
        #     if ship > cap:
        #         days += 1
        #         ship = w
        # if ship:
        #     days += 1
        return days

'''
# 也可以用双层循环来求解所需天数
    def check(self, ws, t, d):
        n = len(ws)
        i = cnt = 1
        total = ws[0]
        while i < n:
            while i < n and total + ws[i] <= t:
                total += ws[i]
                i += 1
            total = 0
            cnt += 1
        return cnt - 1 <= d

# 链接：https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''