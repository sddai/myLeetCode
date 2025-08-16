"""
【核心】此题的本质是，找到当前节点左边第一个比他小的元素，和右边第一个比他小的元素
单调递增栈的入栈、出栈过程如下：
    1. 假设当前进栈元素为 x，如果 x 比栈顶元素小，则直接入栈。
    2. 否则从栈顶开始遍历栈中元素，把小于 x 或者等于 x 的元素弹出栈，直到遇到一个大于 x 的元素为止，然后再把 x 压入栈中。
    3. 【单调栈入栈过程的理解】：每次入栈的元素是递增的，一旦遇到一个比栈顶元素小的值，就从栈中弹出元素
    （3）可以保证弹出来的这个元素是个“洼地”，他左侧的面积就是以他的高度为准计算出来的
"""
# 【解法一】：
'''
我们可以 O(1) 的获取柱体 i 左边第一个比它小的柱体吗？答案就是单调增栈，因为对于栈中的柱体来说，栈中下一个柱体就是左边第一个高度小于自身的柱体。
因此做法就很简单了，我们遍历每个柱体，若当前的柱体高度大于等于栈顶柱体的高度，就直接将当前柱体入栈，否则若当前的柱体高度小于栈顶柱体的高度，说明当前栈顶柱体找到了右边的第一个小于自身的柱体，那么就可以将栈顶柱体出栈来计算以其为高的矩形的面积了。
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        area = 0
        next_smaller = [n for _ in range(n)]
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                next_smaller[stack[-1]] = i
                stack.pop()
            stack.append(i)
        stack = []    
        prev_smaller = [-1 for _ in range(n)]   # 这里应该是-1而不是0
        for i in range(n-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                prev_smaller[stack[-1]] = i
                stack.pop()
            stack.append(i)
        area = 0
        for i in range(n):
            area = max(area, (next_smaller[i] - prev_smaller[i] - 1) * heights[i])
        return area
'''
一个eror：（注意prev_smaller要初始化成-1）
输入
heights =
[1]
添加到测试用例
输出
0
预期结果
1
'''

# 【解法二】
"""
【解题思路】（这种解法略复杂，建议解法一）
    问：如何寻找左侧第一个比当前元素大的元素？
    答：从左到右遍历元素，构造单调递增栈（从栈顶到栈底递增）：
    具体方法：一个元素左侧第一个比它大的元素就是将其「插入单调递增栈」时的栈顶元素。
    如果插入时的栈为空，则说明左侧不存在比当前元素大的元素。
"""
# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         stack_l = []   # 注意stack里边存索引
#         stack_r = []
#         max_l = [0 for _ in range(n)] # 这两个数组用于记录当前点左侧（或者右侧）第一个比他小（或者大）的值
#         max_r = [0 for _ in range(n)] 
#         for i in range(n):
#             while stack_l and heights[stack_l[-1]] >= heights[i]:   # 递增栈
#                  stack_l.pop()
#             max_l[i] = stack_l[-1] if stack_l else -1   # while循环已经把比当前高度大的都弹出去了，所以此时的栈顶是第一个比当前高度小的索引，heights的每个元素的这个索引记录在max_l中
#             stack_l.append(i) # while循环已经把比当前高度大的都弹出去了，此时入栈能保证单调（注意入栈的是索引，存索引是为了求宽度方便）
#         for i in range(n-1, -1, -1):
#             while stack_r and heights[stack_r[-1]] >= heights[i]:
#                 stack_r.pop()   # 栈顶大于当前值，弹出，所以这个while结束之后剩下的栈顶是第一个比当前值小的，这个值决定了面积下限
#             max_r[i] = stack_r[-1] if stack_r else n   # 注意边界条件
#             stack_r.append(i)
#         res = 0
#         for i in range(n):
#             res = max(res, heights[i] * (max_r[i] - max_l[i] - 1))
#         return res if n > 0 else 0

