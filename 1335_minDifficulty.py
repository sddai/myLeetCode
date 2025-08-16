class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp[i][j]表示前i天完成了j项任务花费的最小难度
        # 简单的dp一般是在两种选择里边选min或者max，本题是在所有k的可能值里边选择一个min，所以两层循环里边还需要一层循环遍历k的所有可能取值，其中k表示前i-1天完成了k项任务
        # 也就是说，dp[i][j]是用i天完成j项工作，他地推的前一项应该是前i-1天完成k项工作，第j天完成j-k项工作
        # 所以求k的取值范围：必须满足天数<=任务数,否则，一天至少一个任务，剩下几天没有任务可做
        # 所以i-1<=k且1<=j-k，得：i-1<=k<=j-1
        jobs_num = len(jobDifficulty)
        # dp = [[-1] for _ in range(d+1) for _ in range(jobs_num+1)]   # 注意dp的定义方式
        # dp = [[-1 for _ in range(jobs_num+1)]for _ in range(d+1)] # 有jobs_num+1行，d+1列
        dp = [[float("inf") for _ in range(jobs_num+1)]for _ in range(d+1)] # 有jobs_num+1行，d+1列
        # 【注意】初始化值很重要，这里是-1的话，后边所有求min都会变成-1，所以这里是INF
        dp[0][0] = 0  # 注意还要初始化一天的情况
        m = 0
        for j in range(1, jobs_num+1):
            m = max(m, jobDifficulty[j-1]) # 这里针对第一行的初始化不正确，这样忽略了第一项任务的难度
            # dp[1][j] = m
            dp[1][j] = max(m, jobDifficulty[j-1])
        # for i in range(1, jobs_num+1):    # 此题要注意i,j的内外顺序和含义
        #     for j in range(i, d+1):  # 这里注意j大于等于i，即任务数大于等于天数
        for i in range(2, d+1):    # 此题要注意i,j的内外顺序和含义
            for j in range(i, jobs_num+1):  # 这里注意j大于等于i，即任务数大于等于天数                
                for k in range(i-1, j):
                    dp[i][j] = min(
                        # dp[i][j], dp[i-1][k] + max(jobDifficulty[k+1:j+1])
                        dp[i][j], 
                        dp[i-1][k] + max(jobDifficulty[k:j])
                    )
        print(dp)
        return dp[d][jobs_num] if dp[d][jobs_num] < float("inf")  else -1

'''
分析一个错例：
输入
jobDifficulty =
[9,9,9]
d =
4
输出
null
预期结果
-1


这个错误的原因是，如果完不成任务，则需要返回-1，但是这里边是null
'''
