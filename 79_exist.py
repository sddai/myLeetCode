# 此题与一般回溯的区别在于，回溯的外层还需要套一层循环，用于确定回溯的起点（第一个字符需要从word的第一个字母开始）
# 要注意此题不需要用path记录回溯出来的路径，直接用下标记录即可
# 【注意函数签名及其返回值】
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, path, i, j, idx):
            if idx == len(word):
                # return path
                return True
            if i >= m or i < 0 or j >= n or j < 0:
                return False
                ###
            if board[i][j] != word[idx]:
                return False
            if used[i][j]:
                return False
            used[i][j] = True
            for x,y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                # path.append(board[i][j]) 不用append path
                # used[i][j] = True
                if dfs(board, path, x, y, idx + 1): return True 
                # path.pop()
                # used[i][j] = False
            used[i][j] = False
        # def isValid(board, path, i, j, idx):
        #     # if idx <= len(word) and path[idx] == word[idx]:
        #     # 这句判断不对，此时path还没有append上当前的board[i][j]，应该用board[i][j]判断
        #     if board[i][j] == word[idx]:
        #         return True
        #     else:
        #         return False
            
        # m = len(word)
        # n = len(word[0]) if m else 0
        m = len(board)
        n = len(board[0]) if m else 0        
        path = []
        used = [[False for _ in range(n)] for _ in range(m)]
        # dfs(board, path, 0, 0, 0)
        for i in range(m):
            for j in range(n):
                # if board[i][j] == word[0]:
                    # 别忘了标记used
                    # used[i][j] = True
                    # path.append(board[i][j])
                if dfs(board, path, i, j, 0): return True
                    # used[i][j] = False
                    # path.pop()
        return False 
