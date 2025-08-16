# Hard题
class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(a, b):
            # return abs(a % 6 - b % 6) + abs(a // 6 + b // 6)   # 此题不要将减号写成加号（马虎）
            return abs(a % 6 - b % 6) + abs(a // 6 - b // 6)
        n = len(word)
        ord_A = ord('A')
        dp = [[[float("inf") for _ in range(26)] for _ in range(26)]for _ in range(n+1)]
        # 初始化：i=0的所有dp[0][*][*]都是0
        for i in range(26):
            for j in range(26):
                dp[0][i][j] = 0
                # dp[0][ord(word[0]) - ord_A][i] = 0
                # dp[0][i][j] = 0
        ans = float("inf")
        for i in range(1, n+1):
            curr = ord(word[i-1]) - ord_A #i取值从1到n，表示word中的第i个字母（curr是对应的序号）
            for l in range(26):   # l, r分别表示上一次击键时的左右手指键位
                for r in range(26):  # l, r分别表示上一次击键时的左右手指键位
                    if dp[i-1][l][r] != float("inf"):
                        dp[i][curr][r] = min(dp[i][curr][r], dp[i-1][l][r] + distance(l, curr))
                        dp[i][l][curr] = min(dp[i][l][curr], dp[i-1][l][r] + distance(r, curr))
                    if i == n:
                        ans = min(ans, dp[i][curr][r])
                        ans = min(ans, dp[i][l][curr])
        return ans

# class Solution:
#     def minimumDistance(self, word: str) -> int:
#         def distance(A: int, B: int) -> int:
#             # A = ord(char_a) - ord('A')
#             # B = ord(char_b) - ord('A')
#             x_A = A % 6
#             y_A = A // 6
#             x_B = B % 6
#             y_B = B // 6
#             return abs(x_A - x_B) + abs(y_A - y_B)
#         # 用 dp[i][l][r] 表示在输入了字符串 word 的第 i 个字母后，
#         # 左手的位置为 l，右手的位置为 r，达到该状态的最小移动距离
#         n = len(word)
#         dp = [[[float("inf") for _ in range(26)] for _ in range(26)] for _ in range(n)]   
#         # dp在循环中要求出min，所以dp初值应该是inf，不是0
#         # dp[0][:][:] = 0 # 这样赋初值不对：TypeError: can only assign an iterable
#         # 接下来要对左右手的第一个键赋初值0:【注意这个初值其实是word的第一个字母，也就是word[0]】
#         for i in range(26):
#             dp[0][i][ord(word[0]) - ord('A')] = 0
#             dp[0][ord(word[0]) - ord('A')][i] = 0
#         for i, char in enumerate(word):
#             # A = ord(char) - ord('A')
#             # B = ord(char) - ord('A')
#             curr = ord(word[i]) - ord('A')
#             prev = ord(word[i-1]) - ord('A')
#             # 在这里循环下一个字母的26种情况：
#             for j in range(26):
#                 dp[i][curr][j] = 
#                 # dp[i][A][B] = min(
#                 #     dp[i-1][ord(word[i-1]) - ord('A')][B] + distance(ord(word[i-1])-ord('A'), A), 
#                 #     dp[i-1][A][ord(word[i-1]) - ord('A')] + distance(ord(word[i-1])-ord('A'), B)
#                 # )
#         return (dp[n-1])

