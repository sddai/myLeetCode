def get_block_num(size): 
    BLOCK = 512
    if size % BLOCK == 0:
        return size // BLOCK
    else:
        return (size // BLOCK) + 1

def dp(n, nums):
    Capacity = 1474560
    Block = 512
    m = Capacity // Block
    alist = [0] * n
    for i in range(n):
        alist[i] = get_block_num(nums[i])
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    # dp[i][j]表示用前i个文件装j个block能装的最大总size（总文件大小，也就是背包问题中的value）
    # for i in range(n + 1):
        # dp[i][0] = 1   # 要注意dp的含义，这里是总大小，所以没有可装方案的时候，总大小应该是0，不要误初始化
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # needed = get_block_num(alist[])
            # 装：dp[i - 1][j - alist[i - 1]]
            # 不装：dp[i - 1][j]
            if j - alist[i - 1] >= 0:
                dp[i][j] = max(dp[i - 1][j - alist[i - 1]] + nums[i - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


    
# def dp(n, nums):
#     CAP = 1474560
#     # m = len(nums)
#     dp = [[0, 0] for _ in range(n)]
#     dp[0][0] = 0
#     dp[0][1] = get_size(nums[0])
#     for i in range(1, n):  # 这是贪心，err
#         dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
#         # dp[i][1] = max(dp[i - 1][0] + )
#         curr_size = get_size(nums[i])
#         if dp[i - 1][0] + curr_size <= CAP:
#             dp[i][1] = max(dp[i][1], dp[i - 1][0] + curr_size)
#         if dp[i - 1][1] + curr_size <= CAP:
#             dp[i][1] = max(dp[i][1], dp[i - 1][1] + curr_size)
#     return max(dp[-1][0], dp[-1][1])
    
# n = int(input().strip())
# nums = []
# while True:
#     try:
#         nums.append(int(input().strip()))
#     except:
#         break
n = 3
nums = [737270, 737272, 737288]
print(dp(n, nums))