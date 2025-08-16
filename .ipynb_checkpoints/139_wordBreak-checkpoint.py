# 注意两种写法的区别：
# dp[j] = dp[i] and s[i:j] in word_dict   # 这段代码每一轮循环都要执行，如果后边有不满足条件的情况，dp[j]会被重新刷新，之前遇到的TRUE不会被保留
# if dp[i] and s[i:j] in word_dict: dp[j] = True # 这段代码先判断s[i:j]，满足条件才会更新dp[j]，所以dp不会被后边的值冲掉
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_dict = set(wordDict)
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        # for i in range(1, n + 1):     # 此题思路对但是范围找错了
        #     for j in range(0, i + 1):
        #         for k in range(j, i + 1):
        #             if s[j:k+1] in word_dict:
        #                 dp[k] = dp[j]
        for i in range(n):
            for j in range(i + 1, n + 1):
                # dp[j] = dp[i] and s[i:j] in word_dict
                # dp[j] = dp[i] and (s[i:j] in word_dict)
                if dp[i] and s[i:j] in word_dict:  
                    dp[j] = True

        return dp[-1]