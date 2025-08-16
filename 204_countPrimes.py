class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        cnt = 0
        for i in range(2, n):
            if isPrime[i] == True:
                for j in range(i * i, n, i): 
                    isPrime[j] = False
        for i in range(2, n):
            if isPrime[i] == True:
                cnt += 1
        return cnt
# 对于一个质数 x，如果按上文说的我们从 2x 开始标记其实是冗余的，应该直接从 x⋅x 开始标记，因为 2x,3x,… 这些数一定在 x 之前就被其他数的倍数标记过了，例如 2 的所有倍数，3 的所有倍数等。

# 第二次：
class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n + 1)
        if n >= 0: isPrime[0] = False
        if n >= 1: isPrime[1] = False
        for i in range(2, int(sqrt(n)) + 1):
            if isPrime[i] == True:
                for j in range(i * i, n, i):
                    isPrime[j] = False
        ans = 0
        for i in range(n):
            if isPrime[i]:
                ans += 1
        return ans