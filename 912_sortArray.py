# 此题用快速排序会超时，用例是[2, 2, 2, 2, 2, ..., 2](很多2)
# 关于区间的边界控制需格外小心，稍有不慎就会出错
# 我这里把 i, j 定义为开区间，同时定义：
# [lo, i) <= pivot；(j, hi] > pivot
# 之后都要正确维护这个边界区间的定义
# int i = lo + 1, j = hi;
# 当 i > j 时结束循环，以保证区间 [lo, hi] 都被覆盖
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.n = len(nums)
        self.rand = random.Random()
        self.shuffle(nums)
        self.sort_(nums, 0, self.n - 1)
        return nums

    def sort_(self, nums, left, right):
        # print(nums, left, right)
        if left >= right:
            return 
        p = self.partition(nums, left, right)
        self.sort_(nums, left, p - 1)
        self.sort_(nums, p + 1, right)

    def partition(self, nums, left, right):
        # print(nums, left, right)
        l = left + 1
        r = right
        while l <= r:
            while l < right and nums[l] <= nums[left]:  # 注意不等号（<, <=）边界条件
                l += 1
                # 此 while 结束时恰好 nums[i] > pivot
            while r > left and nums[r] > nums[left]:
                r -= 1
                # 此 while 结束时恰好 nums[j] <= pivot，目标是将小于等于pivot的放在pivot左边，大于pivot的放在右边
            if l >= r:
                break
            # 此时 [lo, i) <= pivot && (j, hi] > pivot
            nums[l], nums[r] = nums[r], nums[l]
        # 【这里漏掉一句话：将pivot与中间值交换】
        # 最后将 pivot 放到合适的位置，即 pivot 左边元素较小，右边元素较大
        # 【注意】两个指针碰在一起的位置，一定满足nums[i] <= pivot
        nums[left], nums[r] = nums[r], nums[left]  # 【为什么是r?——此时左右指针指向同一个数字，l==r,用l，r都一样】，这句的目标是将pivot与中间值交换
        return r

    def shuffle(self, nums):
        n = self.n
        rand = self.rand
        for i in range(n - 1):
            idx = rand.randint(i + 1, n - 1)
            nums[i], nums[idx] = nums[idx], nums[i]
            
            
# 手撕归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def sort_(nums, low, high, tmp):
            if low > high:
                return 
            if low == high:
                return 
            mid = low + (high - low) // 2
            sort_(nums, low, mid, tmp)
            sort_(nums, mid + 1, high, tmp)
            merge(nums, low, mid, high, tmp)
            # return nums

        def merge(nums, low, mid, high, tmp):
            tmp[low:high + 1] = nums[low:high + 1]   # 这样只开辟了一个tmp存储空间，如果tmp是局部变量则每一轮进入函数都要新建存储空间
            l = low
            r = mid + 1
            i = low
            while  i <= high and l <= mid and r <= high and l <= r:
                if tmp[l] <= tmp[r]:
                    nums[i] = tmp[l]
                    l += 1
                    i += 1
                else:
                    nums[i] = tmp[r]
                    r += 1
                    i += 1
            while l <= mid and i <= high:
                nums[i] = tmp[l]
                l += 1
                i += 1
            while r <= high and i <= high:
                nums[i] = tmp[r]
                r += 1
                i += 1


        low = 0
        high = len(nums) - 1
        tmp = nums[:]
        sort_(nums, low, high, tmp)       
        return nums