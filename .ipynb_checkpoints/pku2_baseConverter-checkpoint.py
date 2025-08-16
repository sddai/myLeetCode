def base10_to_N(num: int, N: int) -> int:
    stack = []
    digits = "0123456789ABCDEF"
    while num != 0:
        r = num % N
        num = num // N 
        # if num == 0:
        #     break
        stack.append(r)
        # print("r=", r, "num=", num, "stack=", stack)
    ans = ""
    # print("len:", len(stack))
    for i in range(len(stack)):
        ans = ans + digits[stack.pop()]  # 易错！ 不要写成ans += ans + digits[stack.pop()]，而是 ans = ans + digits[stack.pop()]
        # print(digits[stack.pop()])
        # print(ans)
    return ans


print(base10_to_N(63, 16))
        