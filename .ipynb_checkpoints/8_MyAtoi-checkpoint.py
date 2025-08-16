def myAtoi( s: str) -> int:
    s = s.strip()

    if len(s) == 0:
        return 0

    ifsign = s[0]
    if ifsign == '+':
        sign = 1
        start = 1
    elif ifsign == '-':
        sign = -1
        start = 1
    else:
        sign = 1
        start = 0
    
    val = 0
    for i in range(start, len(s)):
        if not s[i].isdecimal():
            break
        else:
            val = val*10 +int(s[i])
            if sign==1 and val > 2**31 - 1:
                return  2**31 - 1
            if sign==-1 and val > 2**31:
                return -2**31
    
    return val*sign

print(myAtoi("   -1927 3 with some words. ")) # 注意：1927 后边的 3 会被忽略，只有 -1927 会被转换为整数
