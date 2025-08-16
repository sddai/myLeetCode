def calc(num1: str, num2: str) -> str:
    n1 = ""
    n2 = ""
    n = len(num1)
    m = len(num2)
    # for i in range(n):
    #     n1 = n1 + num1[-i]
    # for i in range(m):
    #     n2 = n2 + num2[-1]
    n1 = num1[::-1]
    n2 = num2[::-1]
    # print(n1, n2)
    carry = 0
    res = []
    for i in range(max(m, n) - min(m, n)):
        if n > m:
            n2 = n2 + "0"
        else:
            n1 = n1 + "0"
    for i in range(len(n1)):
        # print(n1[i], n2[i], carry)
        sum_ = int(n1[i]) + int(n2[i]) + carry
        curr = sum_ % 10
        if sum_ >= 10:
            carry = sum_ // 10
        else:
            carry = 0
        # curr = curr + carry
        res.append(curr)
    if carry != 0:
        res.append(carry)
    res = res[::-1]
    return "".join(str(c) for c in res)

result = calc("123", "11")
print(result)
result = calc("1234", "11")
print(result)
result = calc("123456789", "987654321")
print(result)
result = calc("0", "0")
print(result)
result = calc("", "")
print(result)
            
    