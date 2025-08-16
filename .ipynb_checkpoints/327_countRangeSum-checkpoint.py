# 一个思考：
# 【思考】前缀和排序之后，原始序列中的各个数字之间的顺序就改变了，如何将排好序之后的序列与原始序列对应起来？
# 原始数组未排序，但您使用前缀和而不是原始值对其进行排序。 数组的前缀和是从开头到当前索引的所有元素的总和。 例如，如果 nums = [1, -2, 3, 4]，则前缀和为 [0, 1, -1, 2, 6]。 您对前缀和进行排序，而不是对原始值进行排序，因为范围和 S(i, j) 等于 j 处的前缀和减去 i - 1 处的前缀和。例如，S(1, 3) = 5， 等于 6 - 1。
# 【原始数组的顺序不会改变，但前缀和的顺序会改变。】 但是，您仍然可以获得正确的答案，因为您只关心前缀和之间的差异，而不关心它们的绝对值。 当合并两个已排序的一半时，可以使用两个指针来查找满足条件 nums[j] - num <= upper 和 nums[i] - num >= lower 的对，其中 num 是左侧的当前元素 一半。 您可以这样做，因为每一半中的元素都已经排序，因此您可以相应地移动指针。 
# 您不需要知道原始数组中元素的确切索引，只需要知道它们在前缀和数组中的相对位置。
# 另一个问题是，所有的结果一定满足i<j（因为已排序）
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        self.n = len(nums)
        n = self.n
        self.tmp = [0] * (n + 1)   #  tmp是排序前的左右两半，待归并的序列, nums是排好序的序列
        self.lower = lower
        self.upper = upper
        self.count = 0
        preSum = [0] * (n + 1)
        # 【思考】前缀和排序之后，原始序列中的各个数字之间的顺序就改变了，如何将排好序之后的序列与原始序列对应起来？
        # preSum[0] = nums[0]
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        self.sort_(preSum, 0, n)
        return self.count
    
    def sort_(self, nums, left, right):
        if left >= right:
            return 
        mid = left + (right - left) // 2
        self.sort_(nums, left, mid)
        self.sort_(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
    
    
    def merge(self, nums, left, mid, right):
        self.tmp[left:right + 1] = nums[left: right + 1]
        
        i = mid + 1
        j = mid + 1
        for num in nums[left: mid + 1]:
            # while i <= right and  nums[i + 1] - num >= self.lower:
            while i <= right and  nums[i] - num < self.lower:   #（注意小于号） i==right的时候，就是最后一个元素，所以不需要再+1（会越界）
                i += 1
            while j <= right and nums[j] - num <= self.upper:    # nums[j] - num是前缀和
                j += 1
            self.count += j - i
            # j 的值是第一个超过上限的索引，i 的值是第一个满足或超过下限的索引。 因此，有效对的数量是 j - i，而不是 j - i - 1。
        
        # while i <= mid and j <= right:   #【注意如何取前缀和】
        #     while nums[j + 1] - nums[i] >= self.lower and nums[j + 1] - nums[i] <= self.uppper:
        #         # 每一轮固定i，移动j，确定边界处的j之后，[i...j]就是区间个数
        #         j += 1 
        #     self.count += 
        #     i += 1

        i = left
        j = mid + 1
        for p in range(left, right + 1):
            if i == mid + 1:
                nums[p] = self.tmp[j]
                j += 1
            elif j == right + 1:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] < self.tmp[j]:
                nums[p] = self.tmp[i]
                i += 1
            elif self.tmp[i] >= self.tmp[j]:
                nums[p] = self.tmp[j]
                j += 1