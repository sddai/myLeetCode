# 【解法一】双指针解法
    # 1. 注意一个问题：例如左指针从左向右扫描的过程中，不断记录当前点（及其）左侧的最高柱子，因此这个值max_l是递增的
    # max_r同理也是随着向左扫描不断递增的
    # 2. 另一个问题是，只要max_r比max_l大，就能保证从max_l向右一定能装上水位为max_l的水
# 【解法二】dp解法
    # 1. 空间换时间，用两个数组事先把每个点的max_l和max_r记录下来
    # 2. 记录的时候，注意明确max_l的具体含义，问：max_l的计算是否要包含与当前节点height[i]的比较？
    # 答：注意最后求每个柱子处的水面积的时候，是要减去height[i]的
    # 因此，这里计算的max_l是需要将height[i]记录进去的
# 【解法三】单调栈解法
    # 横向求解
# 解法一——双指针解法：
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_l = 0
        max_r = 0
        area = [0 for _ in range(n)]
        area = 0
        while l < r:
            max_l = max(max_l, height[l])
            max_r = max(max_r, height[r])
            if max_l <= max_r:
                area += max_l - height[l]
                # i += 1
                l += 1
            else:   # 这表示max_l>max_r的情况，此时左指针高，右指针低，右指针一定能装上水，注意这种情况的处理：r从右向左移动，因此每次记录max_r-height[i]相当于记录了r指针右侧的水面积
                area += max_r - height[r]
                r -= 1
        return area

# 解法二——dp解法:(这是纵向求解的过程，更直观)（对比单调栈解法，是横向求解）
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [0 for _ in range(n)]
        max_r = [0 for _ in range(n)]
        max_l[0] = height[0] # 注意max_l的初始值如何确定
        # for i in range(2, n):
        #     max_l[i] = max(max_l[i-2], height[i-1])
        for i in range(1, n):
            max_l[i] = max(max_l[i-1], height[i])
        max_r[n-1] = height[n-1]
        # max_r[n-2] = max(0, height[n-1])
        # for i in range(n-3, -1, -1):
        #     max_r[i] = max(max_r[i+2], height[i+1])
        for i in range(n-2, -1, -1):
            max_r[i] = max(max_r[i+1], height[i])
        area = [0 for _ in range(n)]
        print(max_l, max_r)
        for i in range(n):
            area[i] = min(max_l[i], max_r[i]) - height[i]
        return sum(area)
# 第二遍：
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n
        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i + 1])
        area = 0
        for i in range(n):
            if height[i] < min(lmax[i], rmax[i]):
                area += min(lmax[i], rmax[i]) - height[i]
        return area