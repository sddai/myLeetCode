from collections import defaultdict


# 归并排序
def topKFrequent(nums: [int], k: int) -> [int]:
    alist = []
    freq = defaultdict(int)
    for i in nums:
        freq[i] += 1
    for i, num in freq.items():
        alist.append([i, num])  # a[0]是nums中的数，a[1]是计数
    # print(alist)
    # ans = []
    def helper(a: [int], start: int, end: int) -> [int]:
        if start == end:
            return [a[start], ]
        else:
            mid = (start + end) // 2
            left = helper(a, start, mid)
            right = helper(a, mid+1, end)
        ans = []  # 本题注意ans的位置，且ans每次进入递归都要清空，因为后边的递归认为左右两个子序列是排好序的，然后后续递归将上层递归结果得到的两个子序列合并
        while left and right:
            if left[0][1] > right[0][1]:
                ans.append(left.pop(0))
            else:
                ans.append(right.pop(0))
        ans.extend(left if left else right)
        return ans
    res = helper(alist, 0, len(alist)-1)
    result = []
    for i in range(k):
        result.append(res[i][0])
    return result


print(topKFrequent([1,1,1,2,2,3], 2))