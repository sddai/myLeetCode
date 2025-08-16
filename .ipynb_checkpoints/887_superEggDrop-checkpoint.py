# 【用计划递归】+ 【二分搜索】  ->  核心是穷举
# 一个关键的问题：这个【最小值】其实是“试出来”的，即：尝试分别在1-100层扔鸡蛋，【最坏】情况下，正确楼层在剩余尝试次数多的那一边（也就是鸡蛋碎和没碎中比较差的情况，剩余尝试次数多的那种情况），所以取max意味着考虑每种尝试位置的【最坏】情况，然后外边再套一层min，意味着在众多最坏情况下取最小值——“最优的方案、在最坏情况下”：需要多少次？
# 1. 取max是因为要求的是“最坏情况”，也就是要找无论 起始楼层 的初始值如何的条件下的查找次数
#    蛋破碎一定发生在搜索区间穷尽时，不会说你在第 1 层摔一下鸡蛋就碎了，这是你运气好，不是最坏情况。
# 2. 什么叫「至少」要扔几次？
#    如果不限制鸡蛋个数的话，二分思路显然可以得到最少尝试的次数
#    但问题是，现在给你了鸡蛋个数的限制 K，直接使用二分思路就不行了。
# 3. dp数组的定义：dp[k][n]表示当前有 K 个鸡蛋，面对 N 层楼，需要最少的扔dp次鸡蛋
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i][j]表示用i个蛋，一共j层楼的最坏尝试次数
        memo = [[float("inf")] * (n + 1) for _ in range(k + 1)]
        def dp(k, n, memo):
            if k == 1:
                return n
            if n == 0:
                return 0
            if memo[k][n] != float("inf"):
                return memo[k][n]
            l = 1
            r = n
            res = float("inf")
            while l <= r:
                mid = l + (r - l) // 2
                broken = dp(k - 1, mid - 1, memo) + 1
                not_broken = dp(k, n - mid, memo) + 1
                if broken > not_broken:
                    r = mid - 1
                    res = min(res, broken)
                else:
                    l = mid + 1
                    res = min(res, not_broken)
            memo[k][n] = res
            return res
        
        ans = dp(k, n, memo)
        print(memo)
        return ans
        # return memo[-1][-1]
        # 【注意！！！】不要return memo[-1][-1]，这是因为memo只有那些需要的被记录的值才有意义，其他的值都是inf，但是dp是一定能返回有效值的。
                
