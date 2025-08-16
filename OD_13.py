def encode(num: int) -> str:
    binary = bin(num)[2:]
    n = len(binary)
    start = 0
    end = n - 1
    i = n - 1
    ans = []
    while start < i - 6:
        curr_bin = binary[i-6: i+1]  # bin有7位
        curr_bin = "1" + curr_bin
        curr_int = int(curr_bin, 2)
        curr_hex = hex(curr_int)[2:]
        # curr_flag = "1"
        ans.append(curr_hex.upper())
        i = i - 7
    curr_bin = binary[: i + 1]   # 这个bin不一定是7位
    # if len(curr_bin) < 7:
    #     for i in range(7 - len(curr_bin)):
    #         curr_bin = "0" + curr_bin
    curr_int = int(curr_bin, 2)
    curr_hex = hex(curr_int)[2:]
    ans.append(curr_hex.upper())
    res = "".join(c for c in ans)
    if len(res) == 1:
        res = "0" + res
    return res



# # 这段代码没有处理“接下来是否还有剩余”的问题（用0/1表示，放在最高位）——不断递减字符串长度
# def encode(num):
#     K = 7
#     binary = bin(num)[2:]
#     n = len(binary)
#     right = n - 1
#     ans = []
#     remain_bits = n
#     while right - K >= 0:
#         # print(binary[right-K+1: right+1])
#         remain_bits -= K
#         if remain_bits > 0:
#             ans.append("1"+hex(int(binary[right-K+1: right+1], 2))[2:])
#         else:
#             ans.append("0"+hex(int(binary[right-K+1: right+1], 2))[2:])
#         right -= K
#     # print(binary[:right])
#     # print(right)
#     # right += K
#     if right >= 0:
#         ans.append("0" + hex(int(binary[:right+1], 2))[2:])
#     res = "".join(s.upper() for s in ans)
#     length = len(res)
#     if length == 0:
#         res = "00"
#     elif length == 1:
#         res = "0" + res
#     return res

print(encode(100))
print(encode(0))
    