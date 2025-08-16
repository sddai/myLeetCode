# 函数形式的二分法
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        left = 1
        right = 10 ** 9
        while left <= right:
            mid = left + (right - left) // 2
            hour = self.getHour(mid)
            if hour > h:
                # mid = left + 1   # 注意这里不要写反
                left = mid + 1
            else:
                # mid = right - 1
                right = mid - 1
            # elif hour == h:
            #     mid = right - 1
            # elif hour < h:
            #     mid = right - 1 
        return left

    def getHour(self, v):
        hour = 0
        for pile in self.piles:
            hour += pile // v
            if pile % v != 0:
                hour += 1
        return hour