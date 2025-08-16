class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        if n == 0:
            return 0
        dp = collections.defaultdict(int)
        dp[arr[0]] = 1
        for i in range(1, n):
            # if arr[i] - difference in dp:  # 这句话是多余的，因为这样做以后，如果遇到不满足等差条件的就会跳过，这个元素也不会插入到dp里边。我们需要达到的效果是，如果当前元素与前边不构成等差序列，也应该把这个元素插入到dp里边
            dp[arr[i]] = dp[arr[i] - difference] + 1
        # print(dp)
        return max(dp.values())
'''错误解法：此题不能扫描到最后然后返回dp[-1]，原因是以每个元素结尾的子序列的起点不一定是一样的，所以要每一个dp都求出来，然后取max(dp)
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        if n == 0:
            return 0
        find_diff = [set() for _ in range(n)]
        find_diff[0].add(arr[0] + difference)
        for i in range(1, n):
            find_diff[i].add(arr[i] + difference)
            find_diff[i] = find_diff[i] | find_diff[i - 1]
        dp = [0 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 1] + 1 if arr[i] in find_diff[i - 1] else dp[i - 1]
        print(dp)
        return dp[-1]
'''