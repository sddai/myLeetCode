def climbStairs( n: int) -> int:
    dp = [0 for i in range(n+1)]
    print(dp)
    dp[0] = 1
    dp[1] = 1
    print(dp[-1])
    
    if n <= 1:
        return dp[n]
    for i in range(1, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        # print("i=", i)
        # print(dp[i])
        # print(dp[i-1])
        # print(dp[i-2])
        # # print(dp[i-2])
    return dp[n]


print(climbStairs(1))

# dp[-1]就是列表的最后一个元素