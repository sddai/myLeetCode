def thief(balls:set, max_weight:int) -> int:
    # print(balls)
    balls = list(balls)
    # print(balls)
    balls.sort()
    dp = [0 for _ in range(max_weight + 1)]
    dp[0] = 0
    for currSum in range(max_weight+1):
        for ball_weight, ball_value in balls:   # 这里有问题，应该倒序遍历
            # if currSum + ball_weight <= maxweight:
            if currSum >= ball_weight:
                dp[currSum] = max(
                    dp[currSum], 
                    dp[currSum-ball_weight] + ball_value
                )
    return dp[-1]


print(thief({(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}, 20))