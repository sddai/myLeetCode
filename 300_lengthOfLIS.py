# 【解法二】贪心 + 二分查找
# 考虑一个简单的贪心，如果我们要使上升子序列尽可能的长，则我们需要让序列上升得尽可能慢，因此我们希望每次在上升子序列最后加上的那个数尽可能的小。

# 【解法二】解法二，一遍通过
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        s = [nums[0]]
        for i in range(1, n):
            if nums[i] < s[-1]:
                idx = bisect.bisect_left(s, nums[i])
                s[idx] = nums[i]
            elif nums[i] > s[-1]:
                s.append(nums[i])
        return len(s)

# 此题单调栈不对，原因是，单调栈只按照顺序向下保存第一个遇到的单调子序列，但是本文需要找到“最长”的单调子序列（也就是每一个位置上的情况都要考虑到）
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             stack = [nums[i]]
#             for j in range(i, n):
#                 # while stack and nums[j] <= stack[-1]:
#                     # stack.pop()
#                     # continue
#                 if stack and nums[j] > stack[-1]: stack.append(nums[j])
#             ans = max(ans, len(stack))
#         return ans

# 此题第二遍一次通过：
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[-1]