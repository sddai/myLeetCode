# def canJump(nums: [int]) -> bool:
#     l = len(nums)
#     dp = [False for i in range(l)]
#     if l == 0 or l == 1:
#         return True
#     if l == 2:
#         return nums[0] > 0
#     dp[0] = True
#     dp[1] = (nums[0] > 0)
#     for i in range(2, l):
#         for j in range(nums[i]):
#             if(i+j <= l-1):
#                 dp[i+j] = True
#     return dp[l-1]
def canJump(nums:[int]) -> bool:
    n, rightmost = len(nums), 0
    for i in range(n):
        if i <= rightmost:
            rightmost = max(rightmost, i + nums[i])
            if rightmost >= n - 1:
                return True
    return False

print(canJump([3, 2, 1, 0, 4]))