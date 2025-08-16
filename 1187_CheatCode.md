# 1187
```python
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 将arr2排序，方便进行二分查找
        arr2.sort()
        # 由于结果数组严格递增，不可能存在相同元素，可以果断去重
        for i in range(len(arr2)-1, 0, -1):
            if arr2[i] == arr2[i-1]:
                arr2.pop(i)
        n1, n2 = len(arr1), len(arr2)
        # 最大可能替换次数为 min(n1, n2) 即两个数组长度的最小值
        max_step = min(n1, n2)
        inf = 0x3f3f3f3f
        # 构造二维dp数组，dp[i][j]定义：对于子数组arr1，在使用不多于j次替换使得arr1前i个元素的子数组严格递增，前i个元素末尾元素所能达到的最小值，arr1 元素个数从0到n1，元素维度长度为 n1+1，替换次数为0到max_step，操作步数维度长度为 max_step+1
        dp = [[inf] * (max_step + 1) for _ in range(n1 + 1)]
        # 由于 0 <= arr1[i], arr2[i] <= 10^9，最小元素值为0，构造边界-1，方便进行二分查找
        dp[0][0] = -1
        # 用min_step记录使arr1前i个元素的子数组严格递增的最小操作步数，由于min_step随着i的增大一定单调非递减，所以可以单独提出来
        min_step = 0
        for i in range(1, n1 + 1):
            curr_step = inf; # 用curr_step记录当前使arr1前i个元素的子数组严格递增的最小操作步数
            for j in range(min_step, min(i, max_step) + 1):
                # 不进行替换，如果arr1中的当前元素arr1[i-1]比之前i-1个元素构成序列最末尾元素大，直接添加到第i个元素位置
                if dp[i-1][j] < arr1[i-1]:
                    dp[i][j] = arr1[i-1]
                # 如果可替换步数大于0，考虑用arr2中元素替换arr1中元素的情况
                if j > 0:
                    prev = dp[i-1][j-1] # 前i-1个元素前j-1步操作后的末尾元素最小值
                    # 二分查找arr2中比prev大且最接近prev的元素值
                    k = bisect.bisect(arr2, prev)
                    if k < len(arr2): # 如果arr2中存在比prev大且最接近prev的元素值
                        dp[i][j] = min(dp[i][j], arr2[k]); # 取 min(dp[i][j], arr2[k])
                if dp[i][j] != inf: # 如果可以经过最多j步操作使得arr1前i个元素的子数组严格递增
                    curr_step = min(curr_step, j) # 更新curr_step
            if curr_step == inf: # 如果不可以经过最多 min(i, max_step) 步操作使得arr1前i个元素的子数组严格递增
                return -1 # 如果无法让 arr1 严格递增，返回 -1。
            min_step = curr_step # 更新min_step
        return min_step # 返回使 arr1 严格递增所需要的最小操作步数

# 作者：随心源
# 链接：https://leetcode.cn/problems/make-array-strictly-increasing/solutions/1490467/by-sui-xin-yuan-seoj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```