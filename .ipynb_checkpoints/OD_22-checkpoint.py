def split_nums(n, nums):
    preSum = [0] * n
    preSum[0] = nums[0]
    max_abs = -float("inf")
    for i in range(1, n):
        preSum[i] = preSum[i - 1] + nums[i]
    for i in range(n - 1):
        left = preSum[i]
        right = preSum[n - 1] - preSum[i]
        if max_abs < abs(left - right):
            max_abs = abs(left - right)
    return max_abs

n = int(input())
nums = list(map(int, input().split()))
print(split_nums(n, nums))