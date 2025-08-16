def find_treasure(nums):
    n = len(nums)
    preSum = [0] * n
    preSum[0] = nums[0]
    for i in range(1, n):
        preSum[i] = preSum[i - 1] + nums[i]
    ans = -1
    for i in range(n):
        if i == 0:
            left = 0
            right = preSum[n - 1] - preSum[i]
        elif i == n - 1:
            left = preSum[i - 1]
            right = 0
        else:
            left = preSum[i - 1]
            right = preSum[n - 1] - preSum[i]
        if left == right:
            ans = i
    return ans

nums = list(map(int, input().split()))
print(find_treasure(nums))
        