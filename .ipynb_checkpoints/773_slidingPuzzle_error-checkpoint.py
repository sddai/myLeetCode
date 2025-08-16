# 讨论：使用二维数组定位0的位置时更复杂
# 转换成一维数组
# 尝试不转换成一维数组直接求解，结果超时：20/32
import copy
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def findIndex(curr):
            for i in range(m):
                for j in range(n):
                    if curr[i][j] == 0:
                        return i, j
        def isValid(board):#这个函数错在没有把最后一个位置的==0考虑在内，且需要判断的应该是board里边的数字是否满足
            size = m * n
            # num = 1
            for i in range(m):
                for j in range(n):
                    # if num == i * m + j + 1:    
                    # 这里错了：1、应该用board来判断不应该用num，2、矩阵中的第i行j列个数，公式中i行应该乘以n：
                    # if board[i][j] == i * m + j + 1:
                    if board[i][j] == i * n + j + 1:
                        # num += 1
                        continue
                    else:
                        if board[i][j] == 0 and i * n + j + 1 == size:  # 此题错在细节问题：如何确定board[i][j]合法？
                            return True
                        else:
                            return False
            # return True
        m = len(board)
        n = len(board[0]) if board else 0
        q = [board]
        visited = set([])
        res = 0
        while q:
            # print(q)
            size = len(q)
            for i in range(size):
                curr = q.pop(0)
                if str(curr) in visited:
                    continue
                if isValid(curr):
                    return res
                visited.add(str(curr))
                x_0, y_0 = findIndex(curr)
                # print(x_0, y_0)
                print(visited)
                if x_0 + 1 < m and x_0 + 1 >= 0:
                    temp = copy.deepcopy(curr)
                    temp[x_0][y_0], temp[x_0 + 1][y_0] =  temp[x_0 + 1][y_0], temp[x_0][y_0]
                    if str(temp) not in visited: q.append(temp)
                    # print(temp)
                if x_0 - 1 < m and x_0 - 1 >= 0:
                    temp = copy.deepcopy(curr)
                    temp[x_0][y_0], temp[x_0 - 1][y_0] =  temp[x_0 - 1][y_0], temp[x_0][y_0]
                    if str(temp) not in visited: q.append(temp)
                    # print(temp)
                if y_0 + 1 < n and y_0 + 1 >= 0:
                    temp = copy.deepcopy(curr)
                    temp[x_0][y_0], temp[x_0][y_0 + 1] = temp[x_0][y_0 + 1], temp[x_0][y_0]
                    if str(temp) not in visited: q.append(temp)
                    # print(temp)
                if y_0 - 1 < n and y_0 - 1 >= 0:
                    temp = copy.deepcopy(curr)
                    temp[x_0][y_0], temp[x_0][y_0 - 1] = temp[x_0][y_0 - 1], temp[x_0][y_0]
                    if str(temp) not in visited: q.append(temp)
                    # print(temp)
                # break
            res += 1
        return -1

