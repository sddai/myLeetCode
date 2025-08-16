class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        self.tmp = [(0, 0)] * n
        self.arr = []
        # self.count = [0] * n
        self.count = 0
        for i in range(n):
            self.arr.append((i, nums[i]))
        self.sort_(nums, 0, n - 1)
        return self.count
    def sort_(self, nums, left, right):
        if left == right:
            return 
        mid = left + (right - left) // 2
        self.sort_(nums, left, mid)
        self.sort_(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        # print(self.arr)

    def merge(self, nums, left, mid, right):
        tmp = self.tmp
        arr = self.arr 
        # count = self.count 
        # arr_l = [arr[i][1] for i in range(left, mid + 1)]
        # arr_l = []
        # for i in range(left, mid + 1):
        #     arr_l.append(arr[i][1])
        # for j in range(mid + 1, right + 1):
        #     id = bisect.bisect_left(arr_l, 2 * arr[j][1])
        #     print(arr, arr_l, arr[j][1], id)
        #     # if id <= mid - left and  arr_l[id] > 2 * arr[j][1]: self.count += mid - left - id + 2
        #     if id <= mid - left and  arr_l[id] > 2 * arr[j][1]: self.count += left + mid + 1 - id
        tmp[left:right + 1] = arr[left:right + 1]
        # 在此之后，tmp暂存了merge之前的左右两半的数组，nums[]里边的元素经过调换（merge）之后是排序好的数组
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            # 这个循环的逻辑是，每一轮循环固定i，移动j，发现一个满足条件的j，就计算对应的i有多少个（不应该在count中累加j，因为下一轮循环移动j之后会导致j重复计算）
            if arr[i][1] > 2 * arr[j][1]:      # 【易错点】arr是二维的，要取到第二个维度
                self.count += mid - i + 1
                j += 1
            else:
                i += 1
        i = left
        j = mid + 1
        for p in range(left, right + 1):
            if i == mid + 1:
                arr[p] = tmp[j]   # 当i走到尽头的时候，把剩下的j接过来（都比i大）
                # if tmp[i-1][1] > 2 * tmp[j][1]:   # 注意j的取值 
                #     self.count += j - mid -1 
                j += 1
            elif j == right + 1:
                arr[p] = tmp[i]
                # if tmp[i][1] > 2 * tmp[j - 1][1]:   # 注意j的取值 
                #     self.count += j - mid -1 
                i += 1
            elif tmp[i][1] <= tmp[j][1]:
                arr[p] = tmp[i]
                i += 1
            elif tmp[i][1] > tmp[j][1]:
                arr[p] = tmp[j]
                # if tmp[i][1] > 2 * tmp[j][1]:
                #     self.count += j - mid - 1
                j += 1


