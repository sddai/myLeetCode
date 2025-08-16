# 此题几乎一遍通过
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(i, path):
            l = len(path)
            for row in path:
                if row[i] == "Q":
                    return False
            i_1 = i - 1
            l_1 = l - 1
            while i_1 >= 0 and l_1 >= 0:
                if path[l_1][i_1] == "Q":
                    return False
                i_1 -= 1
                l_1 -= 1
            i_2 = i + 1
            l_2 = l - 1
            while i_2 < n and l_2 >= 0:
                if path[l_2][i_2] == "Q":
                    return False
                i_2 += 1
                l_2 -= 1
            return True
        def dfs(n, start):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if used[i]:
                    continue
                if not isValid(i, path):
                    continue
                row = ["." for _ in range(n)]
                row[i] = "Q"
                path.append("".join(row))
                used[i] = True
                dfs(n, i + 1)
                path.pop()
                used[i] = False
        
        used = [False for _ in range(n)]
        res = []
        path = []
        dfs(n, 0)
        return res

# 一种优化方法：使用zip函数
'''
        # 检查右上方是否有皇后互相冲突
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
'''