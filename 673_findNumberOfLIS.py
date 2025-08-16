class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        dp = [[1 for _ in range(2)] for _ in range(n)] # dp[i][0]子序列长度 dp[i][1]子序列个数
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]: # 这表示扫描到的第二个满足递增关系的元素，例如[1, 3, 5, 4, 7]，扫描到4的时候，4处的子序列长度跟5处一样，但是5已经把dp[i][0]更新了，所以二者相等，这时候就要计数增加
                        dp[i][1] += dp[j][1] v
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                ans = dp[i][1]
            elif dp[i][0] == max_len:
                ans += dp[i][1]
        return ans