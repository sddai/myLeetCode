fast power算法的时间复杂度是O(log n)，其中n是指数的大小。这是因为fast power算法利用了指数的二进制表示，每次将指数除以2，直到指数为0为止。这样，计算x^n只需要进行log n次平方和最多log n次乘法，而不是n-1次乘法。例如，如果要计算x^13，我们可以将13写成二进制形式1101，然后有：

x^13 = x^(8+4+1) = x^8 * x^4 * x^1

我们可以通过不断地对x进行平方来得到x^2, x^4, x^8等，然后根据指数的二进制位是否为1来决定是否乘以当前的平方值。这样就可以减少乘法的次数，提高效率。

```python
# 定义一个递归函数，用fast power算法计算幂
def fast_power (base, exp):
    # 如果指数为0，返回1
    if exp == 0:
        return 1
    # 如果指数为负数，返回倒数的幂
    if exp < 0:
        return 1 / fast_power (base, -exp)
    # 计算一半的幂
    temp = fast_power (base, exp // 2)
    # 如果指数为偶数，返回平方
    if exp % 2 == 0:
        return temp * temp
    # 如果指数为奇数，返回平方乘以底数
    else:
        return base * temp * temp

# 测试一些例子
print(fast_power (2, 5)) # 输出32
print(fast_power (3, 6)) # 输出729
print(fast_power (5, -2)) # 输出0.04
```