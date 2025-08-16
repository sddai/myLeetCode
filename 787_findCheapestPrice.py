class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        search_src = collections.defaultdict(list)
        for from_i, to_i, price_i in flights:
            search_src[to_i].append((from_i, price_i))
        dp = [[float("inf")] * (k + 2) for _ in range(n)] # j_max = k + 1
        for j in range(k + 2):
            dp[src][j] = 0   # 经测试，这两种初始化方法都可以
        # dp[src][0] = 0
        # for i in range(n):    
        # 注意i和j的内外顺序，不要反过来：这是由于，我们必须在每个站点的dp值更新完成之后，再考虑下一个站点，对于更新的每一个站点，需要考虑到所有能到达该站点的所有可能起点
        for j in range(1, k + 2):
            for i in range(n):
                for from_i, price_i in search_src[i]:
                    dp[i][j] = min(dp[i][j], dp[from_i][j - 1] + price_i)   # 【易错！】k是常数，这里用j作为变量
        print(dp)
        ans = min(dp[dst][j] for j in range(1, k + 2))
        return ans if ans != float("inf") else -1