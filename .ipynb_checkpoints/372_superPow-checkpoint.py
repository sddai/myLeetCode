class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def pow_(a, b):
            # if b == 0:
            #     return 1
            # res = a % mod_
            # for i in range(b - 1):
            #     res = res * (a % mod_) % mod_   # 超时
            # return res 
            if b == 0:
                return 1
            if b == 1:
                return a % mod_
            if b % 2 == 0:
                # p = pow_(a % mod_, b // 2) % mod_
                # return p * p % mod_
                return pow_((a % mod_) * (a % mod_), b //2)
            else:
                return (pow_((a % mod_) * (a % mod_), b // 2) * a) % mod_
        
        n = len(b)
        mod_ = 1337
        ten = 1
        ans = 1
        # for i in range(n - 1, -1, -1):
        #     pow_num = (b[i] * ten)   
        #     ans = ans * pow_(a, pow_num) % mod_  
        # 这里不对：b的各个数字之间是幂次关系（相乘，不是相加）
        # 而且，pow_num会很大，不要直接求，应该每次取b[i]，这样每次取出来的都是一位数字
        #     ten = ten * 10
        for i in range(n):
            ans = (pow_(ans, 10) * pow_(a, b[i])) % mod_
        return ans
