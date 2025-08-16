import math


def reverse(x: int) -> int:
    result = 0
    while(x != 0):
        tmp = x % 10
        # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
        if x < 0 and tmp > 0:
            tmp -= 10
        # print("tmp: ", tmp)
        if(result > 214748364 or (result ==214749364 and tmp >7) ):
            return 0
        if(result < -214748364 or (result ==-214749364 and tmp + 1 < -8) ):
            return 0 
        result= result*10 + tmp
        x = math.trunc(x / 10) 
    return result            

print(reverse(-123)) #     


'''解法二：都转换成正整数，负数取绝对值
def reverse(x: int) -> int:
# 定义一个变量 y 来存储反转后的结果
    y = 0
    # 定义一个变量 sign 来存储 x 的符号，1 表示正数，-1 表示负数
    sign = 1 if x >= 0 else -1
    # 将 x 转换为绝对值，方便处理
    x = abs(x)
    # 循环反转 x 的每一位数字，并累加到 y 中
    while x > 0:
        # 取出 x 的最低位数字，即个位数
        digit = x % 10
        # 将 y 左移一位，并加上 digit，相当于将 digit 添加到 y 的末尾
        y = y * 10 + digit
        # 将 x 右移一位，即去掉最低位数字
        x = x // 10
    
    # 恢复 y 的符号，即乘以 sign
    y = y * sign
    
    # 判断 y 是否在 32 位有符号整数的范围内，如果不在，则返回 0
    if -2**31 <= y <= 2**31 - 1:
        return y
    else:
        return 0
'''