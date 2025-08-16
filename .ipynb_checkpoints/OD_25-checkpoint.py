def alibaba(nums, k):
    n = len(nums)
    preSum = [0] * n
    preSum[0] = nums[0]
    ans = -float("inf")
    for i in range(1, n):
        preSum[i] = preSum[i - 1] + nums[i]
    for i in range(n - k + 1):
        if i == 0:
            curr = preSum[i + k - 1]
        else:
            curr = preSum[i + k - 1] - preSum[i - 1]
        if ans < curr:
            ans = curr
    return ans
# nums = list(map(int, input().split(",")))
# k = int(input())
nums = [2,10,-3,-8,40,5]
k = 4
print(alibaba(nums, k))