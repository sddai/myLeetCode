class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count = [0] * (n + 1)
        for i in range(n):
            count[nums[i]] += 1
        ans = []
        for i in range(1, n + 1):
            if count[i] == 2:
                ans.append(i)
        for i in range(1, n + 1):
            if count[i] == 0:
                ans.append(i)
        return ans