# 此题的关键：如何找到停止条件？
# 边界上的 O 要特殊处理，只要把边界上的 O 特殊处理了，那么剩下的 O 替换成 X 就可以了。
# 所以此题从边界上的O开始扩散，标记与边界相连接的O，再将所有未标记的O变成X
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, x, y):
            # if x >= m or x < 0 or y >= n or y <= 0:   # 马虎：【这里多了一个等号】
            if x >= m or x < 0 or y >= n or y < 0:
                return False
            # if used[x][y]:  # 已经通过标记#来记录访问过的O，所以不必要使用used
            #     return False
            if board[x][y] != "O":
                return
                # board[x][y] = "#"
            board[x][y] = "#"
            # used[x][y] = True
            for i, j in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                # used[i][j] = True
                dfs(board, i, j)
                # used[i][j] = False
            # used[x][y] = False
        m = len(board)
        n = len(board[0]) if board else 0
        # used = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if board[i][0] == "O": dfs(board, i, 0)
            if board[i][n - 1] == "O": dfs(board, i, n - 1)
        for j in range(n):
            if board[0][j] == "O": dfs(board, 0, j)
            if board[m-1][j] == "O": dfs(board, m - 1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"

'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, x, y, idx, path, res):
            if x >= m or x < 0 or y >= n or y < 0:
                return False
            if used[x][y]:
                return False
            if not isValid(board, x, y, idx, path, res):
                return False
            if idx == m * n:
                return True
            used[x][y] = True   # 相当于isValid == True之后执行这句话
            # path.append([x, y])
            board[x][y] = "X"
            for i, j in [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]:
                if dfs(board, i, j, idx + 1, path, res):
                    return True
            used[x][y] = False
            # path.pop()
            board[x][y] = "O"
        def isValid(board, x, y, idx, path, res):
            if x == 0 or x == m - 1 or y == 0 or y == n - 1:
                return False
            elif board[x][y] == "O":
                return True

        m = len(board)
        n = len(board[0]) if board else 0
        used = [[False for _ in range(n)] for _ in range(m)]
        path = []
        res = []
        dfs(board, 0, 0, 0, path, res)
'''

# 第二次一遍通过
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            if board[i][j] == "#": return 
            if board[i][j] == "X": return 
            board[i][j] = "#"
            if j - 1 >= 0: dfs(board, i, j - 1)
            if i + 1 <= m - 1: dfs(board, i + 1, j)
            if j + 1 <= n - 1: dfs(board, i, j + 1)
            if i - 1 >= 0: dfs(board, i - 1, j)
        m = len(board)
        n = len(board[0])
        for i in range(n):
            if board[0][i] == "O":
                dfs(board, 0, i)
            if board[m - 1][i] == "O":
                dfs(board, m - 1, i)
        for i in range(m):
            if board[i][0] == "O":
                dfs(board, i, 0)
            if board[i][n - 1] == "O":
                dfs(board, i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"