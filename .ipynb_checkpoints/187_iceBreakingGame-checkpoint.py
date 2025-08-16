class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        dp = [0] * num
        dp[0] = 0
        for i in range(1, num):
            # dp[i] = (dp[i - 1] + target) % num
            # dp[i] = (dp[i - 1] + target - 1) % i
            dp[i] = (dp[i - 1] + target) % (i + 1)  
            # i+1 is the current size of the circle
        return dp[-1]
    
# 第二次通过
# https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solutions/177639/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        dp = [0] * num
        # dp[0] = 0 表示最后一轮只剩下一个元素，他的下标是0
        # dp[1] : 在上一轮，剩下这个0号元素前边有target个元素，且target号元素被删除了（此时剩下了i+1=2个元素）
        # 所以 dp[1] = (0+target) % 1   -> 1是这一轮数组的长度
        for i in range(1, num):
            dp[i] = (dp[i - 1] + target) % (i + 1)
        return dp[-1]