# 此题第二遍几乎一次通过
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[float("inf") for _ in range(2)] for _ in range(n)] 
        # dp[i][0]表示不换，dp[i][1]表示换
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                dp[i][0] = min(dp[i-1][0], dp[i][0])
                dp[i][1] = min(dp[i - 1][1] + 1, dp[i][1])
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                dp[i][0] = min(dp[i - 1][1], dp[i][0])
                dp[i][1] = min(dp[i-1][0] + 1, dp[i][1])
        return min(dp[-1]) if min(dp[-1]) != float("inf") else -1

'''
# 这是一类状态机dp
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [[float("inf") for _ in range(2)] for _ in range(n)]   # dp[i][0]表示不更换i号位置导致的次数，dp[i][1]表示更换
        dp[0][0] = 0
        dp[0][1] = 1
        for i in range(1, n):
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i-1]:   # 两个位置或者同时换，或者同时都不换
                dp[i][0] = min(dp[i][0], dp[i - 1][0])
                dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i-1]: # 这种条件下，两个位置只能换一个，例如nums1=[5,6], nums2=[3,7]，此时既满足前一个if的条件，也满足第二个if的条件（第一个if用前一段去计算，这里只计算后一个if，两个if可能同时满足，就都要执行，所以这里不用elif），又比如[5,4]和[3,7]，此时不满足第一个if，只满足第二个if
                # dp[i][0] = min(dp[i][0], dp[i - 1][1] + 1) # 不换不用加1 
                dp[i][0] = min(dp[i][0], dp[i - 1][1]) # 不换不用加1 
                dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)
            # if nums1[i] 
        return min(dp[-1][0], dp[-1][1])
'''

'''
# 【注意控制空间复杂度】：
class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a, b = 0, 1
        for i in range(1, n):
            at, bt = a, b
            a = b = n
            if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
                a = min(a, at)
                b = min(b, bt + 1)
            if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
                a = min(a, bt)
                b = min(b, at + 1)
        return min(a, b)

作者：力扣官方题解
链接：https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/solutions/1879716/shi-xu-lie-di-zeng-de-zui-xiao-jiao-huan-ux2y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# 错误解法
'''
一个没有通过的测试用例：
输入
nums1 =
[3,3,8,9,10]
nums2 =
[1,7,4,6,8]
输出
2
预期结果
1
'''
# class Solution:
#     def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
#         n = len(nums1)
#         dp = [0 for _ in range(n)]
#         for i in range(1, n):
#             if nums1[i] <= nums1[i - 1] or nums2[i] <= nums2[i - 1]:
#                 dp[i] = dp[i - 1] + 1
#             else:
#                 dp[i] = dp[i - 1]
#         return dp[-1]

'''另一种更清晰的解法分成三种情况：
    public int minSwap(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int[][] dp = new int[n][2];
        dp[0][0] = 0;
        dp[0][1] = 1;
        for (int i = 1; i < n; i++) {
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                //当前数字大于前一个数字
                if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                    //当前数字大于另一个数组的前一个数字

                    //前一个交换不交换都无所谓
                    dp[i][0] = Math.min(dp[i - 1][0], dp[i - 1][1]);
                    //交换 + 1
                    dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][1]) + 1;
                } else {
                    //当前数字不大于另一个数组的前一个数字

                    //当前数字不交换，上一个也不能交换
                    dp[i][0] = dp[i - 1][0];
                    //当前数字交换，上一个也必须交换
                    dp[i][1] = dp[i - 1][1] + 1;
                }
            } else {
                //当前数字不大于前一个数字

                //本次不交换 则上一次交换
                dp[i][0] = dp[i - 1][1];
                //本次交换 则上一次不交换
                dp[i][1] = dp[i - 1][0] + 1;
            }
        }
        return Math.min(dp[n - 1][0], dp[n - 1][1]);
    }

作者：京城打工人
链接：https://leetcode.cn/problems/minimum-swaps-to-make-sequences-increasing/solutions/1881055/shi-xu-lie-di-zeng-de-zui-xiao-jiao-huan-y6kb/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

