'''
这是一个典型的回溯
回溯的每一个分支，判断这段字符串是否为回文（使用dp数组来判断）
把这个思路抽象成回溯树，树枝上是每次从头部穷举切分出的子串，节点上是待切分的剩余字符串
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l -1
                dp[i][j] = s[i] == s[j] if j == i + 1 else dp[i+1][j-1] and s[i] == s[j]
        # print(dp)
        # 接下来回溯
        def dfs(s, start):
            # if start == n:
            #     return res
            # if not path:
            #     res.append(path[:])
            if start == n:
                res.append(path[:])
            for i in range(start, n):  # 这句话对应当前节点的所有分叉
                # if dp[start][prev] == True:
                if dp[start][i] == False:   # 注意回溯一般使用continue的形式跳出当前分支（剪枝）
                    continue   # 如果这段不是回文就剪枝
                path.append(s[start:i+1])
                dfs(s, i + 1)
                path.pop()
            # 对比78题子集问题：
            # 78题每一轮在path里边添加的是start之后的那些i所对应的nums[i]，本题每一轮添加的是s[start:i+1]
            # for i in range(start, len(nums)):
                # path.append(nums[i])
                # dfs(nums, i + 1)
                # path.pop()

        path = []
        res = []
        start = 0
        dfs(s, start)
        return res