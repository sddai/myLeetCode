class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # 【注意】dp的初始化：[[0, 0]] * n将建立n个索引，指向同一个数组[0, 0]，修改一个其他的一起变
        # [[0, 0] for _ in range(n)] 将新建n个不同的数组，分别为[0, 0]，修改一个其他的不变
        # dp = [[[0, 0]] * n for _ in range(n)] # 【注意新建数组的方式】用这种方式就无法通过
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # dp[i][j][0]是先手得分，dp[i][j][1]是后手得分
        for i in range(n):
            dp[i][i][0] = nums[i]
            dp[i][i][1] = 0
        # for i in range(n - 1):
        #     dp[i][i + 1][0] = max(nums[i], nums[i + 1])
        #     dp[i][i + 1][1] = min(nums[i], nums[i + 1])
        for i in range(n - 1, -1, -1):   # 【注意】这里是n - 1还是n - 2？————是n - 2（n - 1也可以通过）
            for j in range(i + 1, n, 1):    # 【注意】
                # 【注意】不能直接使用max函数，因为算法需要记录当前做出了哪种选择，以便于更新后手的值
                left = dp[i + 1][j][1] + nums[i]
                right = dp[i][j - 1][1] + nums[j]
                if left >= right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]   # 这意味着，(i, j)处的后手，相当于先手选了一个最优选择之后，在剩下的(i+1, j)里边作为先手选一个（最大的）
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
                # dp[i][j][0] = max(   
                #     dp[i + 1][j][1] + nums[i], 
                #     dp[i][j - 1][1] + nums[j]
                # )
                # dp[i][j][1] = max(
                #     dp[i + 1][j][0] + nums[i], 
                #     dp[i][j - 1][0] + nums[j]
                # )
        # print(dp)
        return dp[0][n - 1][0] >= dp[0][n - 1][1]