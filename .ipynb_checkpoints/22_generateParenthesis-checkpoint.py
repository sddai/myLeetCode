# 【回溯算法】的核心在于穷举+剪枝
# 此题穷举的情况就是在左括号和右括号之间找一个写下来
# 合法括号组合，其子串：左括号的数量都大于或等于右括号的数量
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(n, left, right, start, path, res):
            if left > n or right > n:
                return
            if right > left:
                return 
            if len(path) == n * 2:
                res.append(path[:])
                return 
            path = "".join([path, "("])
            # path.append("(")
            dfs(n, left + 1, right, start + 1, path, res)
            path = path[:-1]

            # path.append(")")
            path = "".join([path, ")"])
            dfs(n, left, right + 1, start + 1, path, res)
            path = path[:-1]
            return res
        start = 0
        path = ""
        res = []
        dfs(n, 0, 0, start, path, res)
        return res
            