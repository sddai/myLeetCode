class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        # 这个dp数组可以用一个isValid函数替换
        for i in range(n):
            for j in range(i, n):
                if j - i + 1 > 3 :
                    continue
                if s[i] == "0" and j > i:
                    # dp[i][j] = False
                    continue
                # if s[i] == "0" and j == i:
                if i == j:
                    dp[i][j] = True
                if j - i + 1 <= 2:
                    dp[i][j] = True
                num = 0
                num += ord(s[i]) - ord("0")
                # for k in range(j, i - 1, -1):  # 这里加反了，应该是左边（高位）不断乘以10
                #     num = num * 10
                #     num += ord(s[k]) - ord("0")
                for k in range(i + 1, j + 1):
                    num = num * 10
                    num += ord(s[k]) - ord("0")
                # if k >= 0 and k <= 255:   # 这里写错了，不是k，是num
                if num >= 0 and num <= 255:
                    dp[i][j] = True    
        def dfs(s, start, res, path):
            # if start == n and len(path) == 4:
            if start == n and len(path) == 4:
                res.append(".".join(path[:]))
            for i in range(start, n):
                if dp[start][i] == False:
                    continue
                if len(path) > 4:
                    continue
                path.append(s[start:i+1])  # 对比78题，主要区别就是78比较nums[i]，本题比较从start到i这串字符
                # dfs(s, start + 1, res, path)   # 这句话调用错了，下一轮应该是从i+1开始，而不是start+1
                dfs(s, i + 1, res, path)
                path.pop()
        # print(dp)    
        start = 0
        res = []
        path = []
        dfs(s, start, res, path)
        return res
                
