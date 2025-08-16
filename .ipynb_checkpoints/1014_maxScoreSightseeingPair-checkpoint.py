def maxScoreSightseeingPair(values: [int]) -> int:
    n = len(values)
    max_of_i = 0
    # max_of_j = 0
    dp = [0 for _ in range(n)]
    for j in range(1, n):
        if j == 1:
            max_of_i = values[j-1]+j-1
            cur_j = values[j] - j
            dp[j] = max_of_i + cur_j
        else:
            max_of_i = max(max_of_i, values[j-1]+j-1)  #两种选项分别对应在当前选择j和不选择j的情况
            cur_j = values[j] - j
            dp[j] = max_of_i + cur_j
    return max(dp)


print(maxScoreSightseeingPair([2, 2, 2]))