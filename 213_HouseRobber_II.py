# 【第二次提交】
# 【环形数组】的处理方法：错位一位，把 1~n 变成 1~n-1 和 2~n
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        res1 = dp[n - 2]
        dp = [0] * n
        dp[0] = 0
        dp[1] = nums[1]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        res2 = dp[n - 1]
        return max(res1, res2)

    
'''def rob( nums ) -> int:
    l = len(nums)
    dp = [0 for i in range(l)]
    if l >=1:
        dp[0] = nums[0]
    if l >= 2:
        dp[1] = max(nums[0], nums[1])
    if l == 1:
        return nums[0]
    if l == 2:
        return max(nums[0], nums[1]) 
    #过了这里能保证l至少是3
    def max_from_start_2_end(start, end): #l>=3
        dp[start] = nums[start]
        dp[start+1] = max(nums[start], nums[start+1])  # 注意进入子函数之后要重新初始化子函数的第一个和第二个dp值
        if end == start+1:  # 这是l为3，max_from_start_2_end长度为2的情况
            return dp[end] 
        if end > start + 1:
            for i in range(start + 2, end + 1):
                dp[i] = max(
                    nums[i] + dp[i-2], 
                    dp[i-1] 
                ) 
                print(f"dp[{i}] = {dp[i]}")    
            for i in range(start + 2, end + 1):
                print(f"---dp[{i}] = {dp[i]}") 
            return dp[end]
    # print(max_from_start_2_end(0, l-2), max_from_start_2_end(1, l-1))
    return max(max_from_start_2_end(0, l-2), max_from_start_2_end(1, l-1))

print(rob([2, 3, 2]))
'''