# 分桶 or 二分
# 此题利用了二分法的如下性质：
# 二分查找返回目标值 val 的索引，对于搜索左侧边界的二分查找，有一个特殊性质：
# 当 val 不存在时，得到的索引恰好是比 val 大的最小元素索引。
# 如果在数组 [0,1,3,4] 中搜索元素 2，算法会返回索引 2，也就是元素 3 的位置，元素 3 是数组中大于 2 的最小元素。
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        s_dict = defaultdict(list)
        res = 0
        for i, c in enumerate(s):
            s_dict[c].append(i)
        # print(s_dict)
        for word in words:
            i = 0  # i用来指向word中的字符位置
            j = -1  # j用来指向s中的字符位置
            # for c in word:
            # for i in range(len(word)):   # 【注意】如果用range来递增i，即使最后一轮产生了break，也会有i==len(word)，所以res会错误的加一，因此这里应该使用while循环而不是for循环
            while i < len(word):
                c = word[i]
                # print(c)
                if c not in s_dict:
                    break
                pos = self.search_left(s_dict[c], j) # 二分查找c在s中第一次出现的位置
                # pos = bisect.bisect_left(s_dict[c], j)
                # print(pos)
                # if find == -1 or find >= len(s_dict[c]):
                # if pos == len(s_dict[c]): # find 其实就是二分法返回的left指针
                if pos == -1 or pos == len(s_dict[c]):
                    # return False
                    break
                # j = find + 1 # 这句有问题：find就是二分法中的left指针，j应该是通过指针取出来的index
                j = s_dict[c][pos] + 1
                i += 1
            if i == len(word):
                res += 1
        return res

    def search_left(self, arr, target):
        n = len(arr)
        left = 0
        right = n - 1
        # while left < n and right >= 0:
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                right = mid - 1
            elif arr[mid] > target:
                right = mid - 1
        # if left < 0 or arr[left] < target:
        # if left < 0: # 左指针从左向右移动，最后应该不超出数组长度
        # if left >= n or arr[left] < target:
        if left >= n:
            return -1
        else:
            return left
        
# 解法二：
        # import bisect
        # def isMatch(word):      
        #     l = -1
        #     for c in word:
        #         index = bisect.bisect_left(pos[c], l + 1)
        #         if index == len(pos[c]): return 0
        #         l = pos[c][index]          
        #     return 1
            
        # pos = {chr(i + ord('a')) : [] for i in range(26)}
        # for i, c in enumerate(s):
        #     pos[c].append(i)

        # return sum(map(isMatch, words))