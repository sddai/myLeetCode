# 约瑟夫环问题，思路是：倒序递推（dp），从最后剩下一个人，这个人是0号，开始向前递推
# 另外就是，i=0是最后1轮，剩下1个元素，i=1是倒数第二轮，剩下2个元素，即i+1个元素
def count(n):
    K = 3
    dp = [0] * n
    # dp[0] = 0
    for i in range(1, n):
        # dp[i] = (dp[i - 1] + K) % n
        dp[i] = (dp[i - 1] + K) % (i + 1)
    return dp[-1] + 1

n = int(input())
print(count(n))