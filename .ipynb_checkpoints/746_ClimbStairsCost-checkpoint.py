def minCostClimbingStairs(cost:[int]) -> int:
    l = len(cost)
    dp = [0 for i in range(l+1)] 
    dp[0] = 0
    dp[1] = 0
    # dp[2] = min(dp[1]+cost[1], dp[0]+cost[0])
    if l <= 1:
        return dp[l]
    for i in range(2, l+1):    # 由于要从倒数第一层或者倒数第二层爬上去(也就是说，除了这l级台阶，还要有一个“楼梯顶部”)，所以要计算最后两层爬上去之后的cost，也就是要多加一层，表示从最后两层爬上来的cost也算在内了，同理初始化dp的时候也要使长度为range(l+1)
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[l]

print(minCostClimbingStairs([10,15,20]))