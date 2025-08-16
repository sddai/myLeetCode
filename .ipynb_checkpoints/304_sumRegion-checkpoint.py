# 此题一遍通过，前缀和
# 优化：还可以降一维
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.sum = [[0] * (n + 1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.sum[i][j + 1] = self.sum[i][j] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_ = 0
        for i in range(row1, row2 + 1):
            sum_ += self.sum[i][col2 + 1] - self.sum[i][col1]
        return sum_



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)