# 注意base case的确定：观察两层for循环，里边有i-1，j-1，（j-2的起始j至少是2），所以需要考虑dp[i][0]和dp[0][j]两类特殊情况：
# dp[i][0]表示使用一行字符串与空正则表达式匹配，肯定匹配不上
# dp[0][j]表示使用一个空字符串与某一个正则表达式匹配，只有p每个偶数位置都是*的时候，才可以匹配
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # TODO 初始化
        dp[0][0] = True
        for j in range(2, n + 1, 2):
            if p[j - 1] == "*": dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # dp[i][j] = dp[i - 1][j - 1] and [i - 1] == p[j - 2] # 这种写法，没有考虑j的前一个是点号'.'的情况
                    # dp[i][j] = dp[i - 1][j - 1] and ([i - 1] == p[j - 2] or p[j - 2] == '.')
                    dp[i][j] = dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') 
                    # 这句的含义是用p[j]的'*'匹配若干个字符，此时，需要当前的s[i]匹配，并且s[i-1]能匹配到p[j]，也就是dp[i-1][j]（注意不是dp[i-1][j-1]，因为后边有考虑到'*'匹配0个字符的情况，所以s[i-1]可以一直匹配到p[j]————即使是匹配0个，也能匹配到p[j]） 
                    # if dp[i - 1][j - 1] == True and s[i] != p[j - 1]:
                    #     dp[i][j] = False
                    # if dp[i - 1][j - 1] == True and s[i] == p[j - 1]:
                    #     dp[i][j] = True 
                    dp[i][j] = dp[i][j] or dp[i][j - 2] # 用'*'匹配0个字符
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[-1][-1]
                