# 注意这和8皇后问题是不一样的：8皇后问题每一行都是新的，但是数独问题中，后边的数字有可能是已经填好的，所以需要把range(9)的所有位置都检测一遍是否冲突，而不能像8皇后问题那样只检测当前位置之前的位置
# 【注意事项】dfs函数必须要有返回接口return！（也就是递归的停止条件）
# 最关键的一句话：
#       if dfs(board, start+1): return True
# 直接用一句话dfs(board, start + 1)递归会导致报错，这会导致即使找到了一个有效的解，函数也会继续向下递归下去，而不会在找到一个解之后就停下来
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, num):
            for j in range(9):   #
                if board[row][j] == num:
                    return False
            for i in range(9):
                if board[i][col] == num:
                    return False
            block_row = row // 3
            block_col = col // 3
            for i in range((block_row)*3, (block_row+1)*3):
                for j in range(block_col*3, (block_col+1)*3):
                    if board[i][j] == num:
                        return False
            return True
        def dfs(board, start):
            row = start // 9
            col =  start % 9
            if start == 81: return True
            if board[row][col] != '.':
                return dfs(board, start + 1)
            # 如果这里不return，调用了dfs之后会接着往下执行，这个已经填好的数字会被覆盖
            # for i in range(81):  # 这里的for循环相当于多叉树的各个分支，有9个分支
            for num in range(1, 10):
                # num = (i % 9) + 1
                # if board[row][col] == "." and isValid(row, col, str(num)):
                if isValid(row, col, str(num)):
                    board[row][col] = str(num) 
                    # dfs(board, start + 1) #直接这么递归会导致报错，这回导致即使找到了一个有效的解，函数也会继续向下递归下去，而不会在找到一个解之后就停下来
                    if dfs(board, start+1): return True
                    board[row][col] = "."
            return False
        dfs(board, 0)


# 这种解法超时
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, num):
            for j in range(col):
                if board[row][j] == num:
                    return False
            for i in range(row):
                if board[i][col] == num:
                    return False
            block_row = row // 3
            block_col = col // 3
            for i in range((block_row)*3, (block_row+1)*3):
                for j in range(block_col*3, (block_col+1)*3):
                    if board[i][j] == num:
                        return False
            return True
        def dfs(board, start):
            row = start // 9
            col =  start % 9
            if start == 81: return 
            for i in range(81):
                num = (i % 9) + 1
                if board[row][col] == "." and isValid(row, col, str(num)):
                    board[row][col] = str(num) 
                dfs(board, start+1)
                board[row][col] = "."
        dfs(board, 0)
'''
