'''把这个问题当作9进制转10进制处理，但因为题中是跳过4而不是9，和一般的进制转换还有差别。

从题目描述来看，如果个位大于4，那么多加了1；十位大于4，多加了10；百位则是100。

因此按照进制转换的思路步骤来做，并在循环中减去多加的部分即可'''


def taxi_fee(num):
    s = str(num)
    n = len(s)
    res = 0
    index = 0
    for i in range(n - 1, -1, -1):
        curr = int(s[i])
        if curr > 4:
            curr -= 1
        res += curr * (9 ** (index))
        index += 1
    return res
print(taxi_fee(25))
print(taxi_fee(5))
print(taxi_fee(17))
print(taxi_fee(100))


# 答案：
# def taxi_fee(num):
    # N_str = str(num)
    # res = 0
    # for i in range(1, len(N_str) + 1):      # i=1...n
    #     N_int = int(N_str[-i])      # -i = -1...-n = n-1 ... 0
    #     if N_int > 4:
    #         N_int -= 1
    #     res += N_int * (9 ** (i-1))   # i-1 = 0...n-1
    # print(res)