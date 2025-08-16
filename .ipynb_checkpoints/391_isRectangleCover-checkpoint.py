# 另见218天际线问题
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x_min = float("inf")
        y_min = float("inf")
        x_max = -float("inf")
        y_max = -float("inf")
        count = defaultdict(int)
        sum_area = 0
        for x1, y1, x2, y2 in rectangles:
            count[(x1, y1)] += 1
            count[(x2, y2)] += 1
            count[(x1, y2)] += 1
            count[(x2, y1)] += 1
            x_min = min(x_min, x1, x2)
            y_min = min(y_min, y1, y2)
            x_max = max(x_max, x1, x2)
            y_max = max(y_max, y1, y2)
            sum_area += abs(x1 - x2) * abs(y1 - y2)
        required_area = (x_max - x_min) * (y_max - y_min)
        if sum_area != required_area:
            return False
        for key, val in count.items():
            if key in ((x_min, y_min), (x_min, y_max), (x_max, y_min), (x_max, y_max)):
                if val == 1:
                    continue
                else:
                    return False
            else:
                if val % 2 != 0:
                    return False
        return True

        
