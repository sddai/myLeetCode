def average2d(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    preSum = [[0] * n for _ in range(m)]
    # preSum[0][0] = matrix[0][0]
    for i in range(m):
        preSum[i][0] = matrix[i][0]
    for j in range(n):
        preSum[0][j] = matrix[0][j]
    # for i in range(1, m):
    #     for j in range(1, n):
    #         preSum[][]
    # for i in range(m):
    row = [[0] * n for _ in range(m)]
    for i in range(m):
        row[i][0] = matrix[i][0]
    for i in range(m):
        for j in range(1, n):
            row[i][j] = row[i][j - 1] + matrix[i][j]
    col = [[0] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(n):
            col[i][j] = col[i - 1][j] + matrix[i][j]
    avg = [[0] * (m - k + 1) for _ in range(n - k + 1)]
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            for t in range(k):
                if j == 0:
                    # avg[i][j] += row[i + k - 1][j + k] - row[i - 1][j + k]
                    avg[i][j] += row[i + t][j + k - 1]
                else:
                    avg[i][j] += row[i + t][j + k - 1] - row[i + t][j - 1]
                    # avg[i][j] += row[i + k - 1][j + k] - row[i - 1][j + k]
            # if i == 0:
            #     avg[i][j] = row[i + k - 1][j]
            # else:
            #     avg[i][j] = row[i + k -1][j] - row[i - 1][j]
    for i in range(m - k + 1):
        for j in range(n - k + 1):
            avg[i][j] /= k * k
    return avg

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(average2d(matrix, 2))