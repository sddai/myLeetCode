from collections import defaultdict
'''
用堆排序求前K个最大值，用小顶堆：
每次比较，如果堆顶更大，说明至少有k个数字的出现次数比当前值大，故舍弃当前值；否则，就弹出堆顶，并将当前值插入堆中。

注意：此答案直接heap_sort是不符合要求的，因为有时间复杂度要求
'''
def topKFrequent(nums: [int], k: int) -> [int]:
    n = len(nums)
    count_dict = defaultdict(int)
    for i in range(n):
        count_dict[nums[i]] += 1
    alist = [None, ]
    for key, value in count_dict.items():
        alist.append([key, value])
        # alist[i][0]是原数字，alist[i][1]是要排序的出现次数
    size = len(alist) - 1
    def heapify(alist: [[int]], i: int) -> None:   # 可以理解为，一次heapify相当于顺着一个元素，排序了从根到叶子的一条路径
        for i in range(i, 0, -1):     # 这里不好，heapify不用循环，而应该每次递归更换的那个节点
            max = i
            # if alist[2 * i] and alist[2 * i][1] > alist[max][1]:   # 这里不对，因为2*i有可能超过数组下标导致越界
            if 2 * i < size and alist[2 * i][1] > alist[max][1]:
                max = 2 * i
            if 2 * i + 1 < size and alist[2 * i + 1][1] > alist[max][1]:
                max = 2 * i + 1
            if max != i:
                alist[max], alist[i] = alist[i], alist[max]
    heapify(alist, size // 2)  # heapify一次以后，根最大
    def heap_sort(alist: [[int]], size: int) -> None:
        largestK = []
        for j in range(k):
            largestK.append(alist[1][0])
            alist[1] = alist[size]
            size = size - 1
            heapify(alist, size // 2)
        return largestK
    return heap_sort(alist, size)



