# (几何题)扫描线法：求解差分信息
# 容易忽略的一个关键点：buildings坐标都是整数，见函数签名`buildings: List[List[int]]`
# 使用heapq的难点在于如何实现remove by key?  —— 解法一：SortedDict，解法二：heapq
# 解释为什么不用SortedSet而使用SortedDict：
# Set遇到重复元素只保存一个，如果遇到了同一高度、不同横坐标的若干座建筑，则remove一次之后Set里边就不再有这个楼的高度了
# 所以用defaultdict(list)，这样可以通过将list里边的heights加入sortedList，再逐个pop的方式，处理相同高度的建筑
# 注意处理高度平齐的并排两座建筑
from sortedcontainers import SortedList
# import heapq
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # heights = SortedSet()
        # points = SortedSet()
        heights = SortedList()
        points = SortedList()
        ans = {}
        n = len(buildings)
        for l, r, h in buildings:
            points.add((l, h))
            points.add((r, -h))
        prev = 0
        curr = SortedList()
        for i, h in points:
            if h > 0:
                curr.add(h)
                # heapq.heappush(curr, h)
            else:
                curr.remove(-h)
                # heapq.heappop(curr, -h)  # 这里使用sortedSet或者heapq都不合适，所以用sortedDict
            if curr:
                ans[i] = curr[-1]   # ans[i]里边暂存了每个跳变点处的最高建筑高度，i是对应横坐标
                # 但是要注意，ans中的i作为跳变点，不意味着最终结果里边包括ans中的每一个i，因为两个跳变点处高度可能是一致的
            else:
                ans[i] = 0
        k = sorted(ans.keys())
        res = []
        last = None
        for i in k:
            # if ans[i] != last:
            if True:
                res.append([i, ans[i]])  # 这部分扫描ans，如果ans中有重复的高度，就放弃后边的
                last = ans[i]
        return res
        # for i, h in points:
        #     # curr = heights[-1]
        #     if h > 0:
        #         # curr = heights[-1]
        #         heights.add(h)
        #     else:
        #         # curr = heights[-1]
        #         heights.remove(-h)
        #     curr = heights[-1]
        #     # if abs(curr) == prev:
        #     #     continue
        #     # ans.append([i, abs(curr)])
        #     # prev = abs(curr)
        #     if abs(curr) != prev:
        #         ans.append([i, abs(curr)])
        #         prev = curr 
        return ans
    
# # example:
# from sortedcontainers import SortedList
# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         dic={}
#         for i in buildings:
#             a,b,c=i[0],i[1],i[2]
#             if a not in dic:
#                 dic[a]=[c]
#             else:
#                 dic[a].append(c)
#             if b not in dic:
#                 dic[b]=[-c]
#             else:
#                 dic[b].append(-c)
#         keys=sorted(dic.keys())
#         ans={}
#         cur=SortedList()
#         for i in keys:
#             for j in dic[i]:
#                 if j>0:
#                     cur.add(j)
#                 else:
#                     cur.remove(-j)
#             if cur:
#                 ans[i]=cur[-1]
#             else:
#                 ans[i]=0
#         k=sorted(ans.keys())
#         res=[]
#         last=None
#         for i in k:
#             if ans[i]!=last:
#                 res.append([i,ans[i]])
#                 last=ans[i]
#         return res

# # 注意处理高度平齐的并排两座建筑
# from sortedcontainers import SortedSet
# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
#         heights = SortedSet([0])
#         points = SortedSet()
#         ans = []
#         n = len(buildings)
#         for l, r, h in buildings:
#             points.add((l, h))
#             points.add((r, -h))
#         prev = 0
#         for i, h in points:
#             # curr = heights[-1]
#             if h > 0:
#                 # curr = heights[-1]
#                 heights.add(h)
#             else:
#                 # curr = heights[-1]
#                 heights.remove(-h)
#             curr = heights[-1]
#             # if abs(curr) == prev:
#             #     continue
#             # ans.append([i, abs(curr)])
#             # prev = abs(curr)
#             if abs(curr) != prev:
#                 ans.append([i, abs(curr)])
#                 prev = curr 
#         return ans