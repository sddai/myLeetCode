# 【注意】当nums中没有重复元素的时候，可以使用字典将num映射到index，但是如果nums存在重复元素，可以使用元组(idx, val)存储对应的索引下标
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort_(pairs, left, right):
            if left == right:
                return 
            mid = left + (right - left) // 2
            sort_(pairs,  left, mid)
            sort_(pairs,  mid + 1, right)
            merge(pairs,  left, mid, right)
            # tmp = pairs
            # for i in range(left, right + 1):
                # if pairs[left][1] < pairs[][]
        def merge(pairs, left, mid, right):
            # print(tmp)
            # 最后要对pairs进行排序，所以要有一个tmp暂存原始数据
            for i in range(left, right + 1):
                tmp[i] = pairs[i]
            i = left
            j = mid + 1
            # p = left
            # for i in range(left, right + 1):
            # while i <= mid and j <= right and p <= right:
            for p in range(left, right + 1):
                # print(i, j)
                # 这里注意增加i，j超过边界的问题
                if i == mid + 1:
                    # tmp[p] = pairs[j][1]
                    pairs[p] = tmp[j]
                    j += 1
                    # p += 1
                elif j == right + 1:   # 右半边走到尽头，把i（左半边）接过来，且j停下来的位置是最小值，整个右半边都比i小
                    # tmp[p] = pairs[i][1]
                    pairs[p] = tmp[i]
                    i += 1
                    # p += 1
                    # 【这里勿忘更新counts！】
                    counts[pairs[p][0]] += j - mid -1
                # elif pairs[i][1] > pairs[j][1]:
                elif tmp[i][1] > tmp[j][1]:
                # else:
                    # tmp[p] = pairs[j][1]
                    pairs[p] = tmp[j]
                    # counts[pairs[j][0]] += j - i - 1 # 注意是减去mid，不是减去i
                    # 左半边，i后边的都比i大，右半边，j比i小，所以，在右半边中j及其前边的，都比i小
                    # counts[pairs[j][0]] += j - mid - 1
                    # counts[pairs[p][0]] += j - mid - 1
                    # print(j - mid - 1)
                    j += 1
                    # p += 1
                # elif pairs[i][1] <= pairs[j][1]:
                # elif tmp[i][1] < tmp[j][1]:  # 【注意】tmp用于暂存原来的左右两个半边，pairs中存储新的排序后的数字
                else:
                    # tmp[p] = pairs[i][1]  # # 最后要对pairs进行排序，所以要有一个tmp暂存原始数据
                    pairs[p] = tmp[i]
                    counts[pairs[p][0]] += j - mid - 1
                    # print(j - mid - 1)
                    i += 1
                    # p += 1

        pairs = []
        n = len(nums)
        # pairs = []
        for i in range(n):
            pairs.append((i, nums[i]))
        # print(pairs)
        # tmp = pairs[:]
        tmp = [(0, 0) for _ in range(n)]
        counts = [0] * n
        # print(counts)
        sort_(pairs, 0, n - 1)
        # res = [c for c in counts]
        return counts
        # return res
        
