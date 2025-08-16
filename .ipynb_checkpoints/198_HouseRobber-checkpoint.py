def rob(nums: [int]) -> int:
    l = len(nums)
    dp = [0 for i in range(l)]
    dp[0] = nums[0]
    if l >= 2:
        dp[1] = max(nums[1], 
                    dp[0])
    if l == 0: return 0
    if l <= 2: return dp[l-1] 
    for i in range(2, l):
        dp[i] = max(
            nums[i] + dp[i-2], 
            dp[i-1]
        )
    return dp[l-1]

print(rob([1,2,3,1]))

'''
# 第二次提交：
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp = [[0] * 2 for _ in range(n)] # dp[i][0]不取，dp[i][1]取
        dp[0][0] = 0
        dp[0][1] = nums[0]
        dp[1][0] = nums[0]
        dp[1][1] = nums[1]
        for i in range(2, n):
            dp[i][0] = max(
                dp[i][0], 
                dp[i - 1][0], 
                dp[i - 1][1]
            )
            dp[i][1] = max(
                dp[i][1], 
                dp[i - 2][1] + nums[i], 
                dp[i - 1][0] + nums[i]
            )
        return max(dp[-1][0], dp[-1][1])
'''