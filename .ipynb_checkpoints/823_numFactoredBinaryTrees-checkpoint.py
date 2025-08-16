def numFactoredBinaryTrees(arr: [int]) -> int:
    # dp = defaultdict(int)
    arr.sort()   # 先排序，后取index
    n = len(arr)
    arr_set = set(arr)
    dp = [1 for _ in range(n)]
    index = {x:i for i,x in enumerate(arr)}
    for i in range(n):
        for j in range(i):
            # 在循环里边判断能否整除：
            if arr[i] % arr[j] == 0:
                num = arr[i] / arr[j]
                if num in arr_set:
                    # dp[i] = (dp[i] + dp[i] * dp[j]) % (10**9 + 7)
                    # dp[i]是积，dp[j]和num是两个乘数，num在dp中的下标是index[num]
                    dp[i] = (dp[i] + dp[j] * dp[index[num]]) 
                    dp[i] = dp[i] % (10**9 + 7)
    # print(dp)
    # return dp[-1]   # 注意返回的是所有可能结果，而不是最后一个值
    return sum(dp) % (10**9 + 7)


print(numFactoredBinaryTrees([2,4,5,10]))
        