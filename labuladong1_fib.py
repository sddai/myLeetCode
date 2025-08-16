# 带备忘录形式的递归（用于理解动态规划）
def fib(i, dp):
    if dp[i] != -float("inf"):
        return dp[i]
    if i == 0 or i == 1 or i == 2:
        return 1
    return fib(i - 1, dp) + fib(i - 2, dp)

    
N = 20
dp = [-float("inf") for _ in range(N + 1)]
print(fib(N, dp))