# 此题一遍通过
# 【优化效率】：可以考虑将字典换成dp数组中的四个元素（dp换成n*4的二维数组）
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 5
        dp = [0 for i in range(n + 1)]
        dp[0] = 0
        dp[1] = 5
        count = dict({'a':1, 'e':1, 'i':1, 'o':1, 'u':1})
        for i in range(2, n + 1):
            cnt_a = count['a']
            cnt_e = count['e']
            cnt_i = count['i']
            cnt_o = count['o']
            cnt_u = count['u']
            dp[i] = (cnt_a * 1 + 
                    cnt_e * 2 +
                    cnt_i * 4 +
                    cnt_o * 2 +
                    cnt_u * 1) % (10**9 + 7)
            count['a'] = cnt_e + cnt_i + cnt_u
            count['e'] = cnt_a + cnt_i
            count['i'] = cnt_e + cnt_o
            count['o'] = cnt_i
            count['u'] = cnt_i + cnt_o
        return dp[-1]
