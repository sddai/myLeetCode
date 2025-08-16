# 【解法一】dp
# 【解法二】用dfs（回溯）遍历（穷举）每个位置上的所有选择（例如godding，两个d，分别递归），此外，顺时针逆时针旋转也是两种选择方式
# 对于key（目标）中的一个字符（例如d），在ring中找到他对应的所有索引: dfs(i, j): ring对齐i时从key[j]到末尾需要的步数 
# 题解：https://leetcode.cn/problems/freedom-trail/solutions/1/python3-lai-ba-zhan-shi-shi-shi-ju-zhuquan-guo-zui/
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        n = len(key)
        char_index = collections.defaultdict(list)
        for i, c in enumerate(ring):
            char_index[c].append(i)
        dp = [[float("inf")] * (n + 1) for _ in range(m)]   # dp有n+1列，原因是需要一列来存储“全拼完”的状态，这个状态下cost是0
        # dp[-1][-1] = 0
        for i in range(m):  # 注意dp数组的初始化
            dp[i][-1] = 0
        # for i in range(m):
        for j in range(n - 1, -1, -1):
            for i in range(m):
                for k in char_index[key[j]]:
                    # 这里的含义是，dp[i][j]表示时钟对准ring上的i号字母，为了拼出key[j:]这串字符需要的步数
                    # 这三个循环遍历的是，首先对于j，反向遍历key中的每一个目标字母
                    # 然后遍历ring上的每一个可能的时钟对准位置i
                    # 对于这些可能的位置，需要把时钟从位置i移动到位置key[j]（也就是k）
                    step = min(abs(i - k), m - abs(i - k)) + 1  # 注意这里是i不是j，因为要计算的是ring从i转到k需要的步数
                    dp[i][j] = min(dp[i][j], dp[k][j + 1] + step)
        # print(dp)
        return dp[0][0]
        
        
        # n = len(ring)
        # m = len(key)
        # dp = [[0] * (m + 1) for _ in range(n + 1)]
        # char_idx = collections.defaultdict(list)
        # for idx, c in enumerate(ring):
        #     char_idx[c].append(idx)
        # for i in range(n, -1, -1):
        #     for j in range(1, m + 1):
        #         for idx in char_idx[key[j - 1]]:
        #             step = min(abs(idx - i), n - abs(idx - i))
        #             dp[i][j] = min(
        #                 dp[i][j],
        #                 dp[idx][j + 1] + step + 1
        #             ) if dp[i][j] != 0 else dp[idx][j + 1] + step + 1
        # return dp[0][0]

        # for i in range(1, n + 1):
        #     if ring[i - 1] == key[-1]:
        #         dp[i][-1] = 1
        # for i in range(n, -1, -1):
        #     for j in range(m, -1, -1):
        #         dp[i][j] = min(
        #             dp[i][j - 1] + abs(i - ), # 【注意】 这里难以确定上一轮i的索引，解决方案是，使用一个字典记录ring中每个字符的index

        #         )