# 这个题目一个比较好的地方是：给的数字是 1−N1-N1−N 的全排列，所以我们每次要找哪个数字很容易确定，不需要 O(N)O(N)O(N) 的遍历去判断最大的数字是谁。
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def pan(arr, k):
            for i in range((k) // 2 + 1):
                # arr[i], arr[k - 1 - i] = arr[k - 1 - i], arr[i]
                arr[i], arr[k - i] = arr[k - i], arr[i]
        n = len(arr)
        # max_index = 0
        # max_num = arr[0] # 注意每轮循环都要更新max_index的值
        res = []
        for t in range(n - 1, -1, -1):
            max_index = 0
            max_num = arr[0]
            for i in range(t + 1):
                if arr[i] > max_num:
                    max_index = i
                    max_num = arr[i]
            # print(t)
            if max_index == t:
                continue
            pan(arr, max_index)
            # print("max_index: ", max_index, arr)
            res.append(max_index + 1)
            pan(arr, t)
            # print("max_index: ", max_index, arr)
            res.append(t + 1)
        return res