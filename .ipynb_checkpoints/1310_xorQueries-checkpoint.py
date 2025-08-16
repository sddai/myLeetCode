class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 直接转二进制会超时
        # def base2(arr: int) -> [int]:
        #     res = []
        #     while arr != 0:
        #         res.append(arr % 2)
        #         arr = arr // 2
        #     for i in range(len(res) // 2):
        #         res[i], res(len(res) - i - 1) = res(len(res) - i - 1), res[i]
        #     return res
        n = len(arr)
        xors = [-1 for i in range(n)]
        xors[0] = arr[0]
        for i in range(1, n):
            xors[i] = arr[i] ^ xors[i-1]
        res = []
        for L, R in queries:
            if L == 0:
                res.append(xors[R])
            else:
                res.append(xors[R] ^ xors[L-1])
        return res
        