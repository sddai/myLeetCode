def maxArea(height: [int]) -> int:
    # 双指针法：每次移动 数字较小的那个指针
    n = len(height)
    left = 0
    right = n -1
    area = 0
    while left != right:
        area = max(
            area, 
            (right - left) * min(height[left], height[right])
        )
        if height[left] < height[right]:  # 这里不要比较left和right，而应该比较height[left]和height[right]
            left = left + 1
        else:
            right = right -1
    return area


print(maxArea([1,8,6,2,5,4,8,3,7]))

"""
第二次刷到此题：
# 解题的核心思路是“短板理论”：水的多少由短板决定，两块板子一长一短，移动长的，下限不变（宽度减一），移动短的，下限有可能会变，所以每次都移动短的那个指针
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n-1
        area = 0
        while left != right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
"""

"""
# 再次重刷：
# 如果移动较低的那一边，那条边可能会变高，使得矩形的高度变大，进而就「有可能」使得矩形的面积变大；相反，如果你去移动较高的那一边，矩形的高度是无论如何都不会变大的，因为此时短边不变，除非移动之后那条边更短，面积会更小
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        res = 0
        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)
            res = max(res, curr_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
"""

"""
这种做法超时了：
        n = len(height)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                width_box = j - i
                height_box = min(
                    height[i], 
                    height[j]
                )
                dp[i][j] = width_box * height_box
                if dp[i][j] > ans:
                    ans = dp[i][j]
        return ans
"""