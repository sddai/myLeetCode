'''此题第二遍一次通过：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-float("inf") for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
'''


def maxSubArray( nums:[int]) -> int:
    n = len(nums)
    dp = [0 for _ in range(n)]
    for i in range(n):
        if i == 0:
            dp[i] = nums[i]
        else:
            dp[i] = max(
                dp[i-1] + nums[i], 
                nums[i]
            )
    return max(dp)


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


'''
# 前缀和方法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * n
        preSum[0] = nums[0]
        for i in range(1, n):
            preSum[i] = preSum[i - 1] + nums[i]
        min_ = 0
        res = -float("inf")
        for i in range(n):
            if i == 0:
                min_ = 0
                res = preSum[0]
                print(i, min_, res)
                continue
            min_ = min(
                min_, 
                preSum[i - 1]
            )
            res = max(
                res, 
                preSum[i] - min_
            )
            print(i, preSum[i], min_, res)

        return res

'''