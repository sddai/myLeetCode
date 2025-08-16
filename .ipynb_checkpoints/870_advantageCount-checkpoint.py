# 田忌赛马的解题思路：【用双指针，从最快的马开始，比得过就比，比不过就送】
# 将齐王和田忌的马按照战斗力排序，然后按照排名一一对比。
# 如果田忌的马能赢，那就比赛，如果赢不了，那就换个垫底的来送人头，保存实力。
# 更进一步的，根据这个思路，我们需要对两个数组排序，但是 nums2 中元素的顺序不能改变
# 因为计算结果的顺序依赖 nums2 的顺序，所以不能直接对 nums2 进行排序，而是利用其他数据结构来辅助。
# 可以使用SortedList或者heapq来解题
from sortedcontainers import SortedList
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        sorted_nums2 = SortedList(key = lambda x: x[1])
        for i, num in enumerate(nums2):
            sorted_nums2.add((i, num))
        nums1.sort()
        res = [None] * n
        left = 0
        right = n - 1
        # while left <= right:
        for i in range(n - 1, -1, -1):
            if nums1[right] > sorted_nums2[i][1]:
                res[sorted_nums2[i][0]] = nums1[right]
                right -= 1
            else:
                res[sorted_nums2[i][0]] = nums1[left]
                left += 1
        return res
    
# 解法二
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums2_q = []
        for i, num in enumerate(nums2):
            nums2_q.append((-num, i))
        # nums2_q = heapq.heapify(nums2_tmp)   # heapify返回空，是inplace的
        heapq.heapify(nums2_q)
        nums1.sort()
        print( nums2_q)
        res = [0] * n  # 用 0 比用 None 效率更高
        left = 0
        right = n - 1
        # print(nums2_q)
        for i in range(n-1, -1, -1):
            curr = heapq.heappop(nums2_q)
            if nums1[right] > -curr[0]:
                res[curr[1]] = nums1[right]
                right -= 1
            else:
                res[curr[1]] = nums1[left]
                left += 1
        return res

'''
# 另一种更高效的解法：只存储num1和num2的index
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        idx1, idx2 = list(range(n)), list(range(n))
        idx1.sort(key=lambda x: nums1[x])
        idx2.sort(key=lambda x: nums2[x])

        ans = [0] * n
        left, right = 0, n - 1
        for i in range(n):
            if nums1[idx1[i]] > nums2[idx2[left]]:
                ans[idx2[left]] = nums1[idx1[i]]
                left += 1
            else:
                ans[idx2[right]] = nums1[idx1[i]]
                right -= 1
        
        return ans

作者：力扣官方题解
链接：https://leetcode.cn/problems/advantage-shuffle/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''