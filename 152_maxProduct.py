def maxProduct( nums: [int]) -> int:
    n = len(nums)
    dp = [[0 for i in range(n) ] for _ in range(2)]
    # dp[0][]存最小值
    # dp[1][]存最大值
    for i in range(n):
        if i == 0:
            dp[0][i] = nums[i]
            dp[1][i] = nums[i]
        else:
            if nums[i] > 0:
                dp[0][i] = min(nums[i], nums[i]*dp[0][i-1])
                dp[1][i] = max(nums[i], nums[i]*dp[1][i-1])
            if nums[i] == 0:
                dp[0][i] = 0
                dp[1][i] = 0
            if nums[i] < 0:
                dp[0][i] = min(nums[i], nums[i]*dp[1][i-1])
                dp[1][i] = max(nums[i], nums[i]*dp[0][i-1])
    return max(dp[1])


print(maxProduct([-2,1,-3,4,-1,2,1,-5,4])) 
print(maxProduct([-2,0,-1]))