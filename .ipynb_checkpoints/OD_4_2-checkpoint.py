# 输入获取
m, t, p = map(int, input().split())  # 故障确认周期数m, 故障次数门限t, 故障恢复周期数p
s = list(map(int, input().split()))  # 一段周期的采样数据列表
 
# 全局变量
NORMAL = 1  # 正常数据的状态
FAULT = 2  # 错误数据的状态
ABORT = 3  # 丢弃的状态
RECOVERY_NORMAL = 4  # 故障恢复检查期间的正常数据的状态
RECOVERY_FAULT = 5  # 故障恢复检查期间的错误数据的状态
 
# 记录每个采样数据的状态
status = [0] * (len(s))
 
 
# 正常期间检查
def check_normal(i):
    if s[i] <= 0:
        return False
 
    # 和前面采样数据比较的前提条件是：前面的采样数据必须是正常状态，或者正常期错误状态
    if i >= 1 and (status[i-1] == NORMAL or status[i-1] == FAULT):
        if s[i] < s[i-1]:
            return False
        if s[i] - s[i-1] >= 10:
            return False
 
    return True
 
 
# 故障恢复期间检查
def check_recovery(i):
    if s[i] <= 0:
        return False
 
    # 和前面采样数据比较的前提条件是：前面的采样数据不能时丢弃状态，以及恢复期错误状态
    if i >= 1 and status[i-1] != ABORT and status[i-1] != RECOVERY_FAULT:
        if s[i] < s[i - 1]:
            return False
        if s[i] - s[i - 1] >= 10:
            return False
 
    return True
 
 
# 算法入口
def getResult():
    # M个周期可以当成滑窗，l是滑窗的左边界, r是滑窗的右边界
    l, r = 0, 0
 
    # 滑窗内错误数据的个数
    window_fault_count = 0
 
    # 滑窗右边界纳入新数据
    while r < len(s):
        # 如果滑窗长度超过了m，那么滑窗的左边界需要右移
        if r - l + 1 > m:
            # 如果右移前的，滑窗左边界对于的数据状态是FAULT，则右移后的滑窗内错误数据个数-1
            if status[l] == FAULT:
                window_fault_count -= 1
            l += 1
 
        # 检查数据状态
        if check_normal(r):
            # 如果数据正常，则标记status[r]为正常状态
            status[r] = NORMAL
        else:
            # 如果数据异常，则需要检查当前数据前面一个数据的状态
            if r < 1 or status[r-1] == ABORT:
                # 如果当前数据前面一个数据的状态是丢弃的，则当前数据没有代替值，也需要被丢弃
                status[r] = ABORT
                # 一旦出现丢弃数据，则滑窗中断，此时需要重置滑窗
                window_fault_count = 0
                l = r + 1
            else:
                # 如果当前数据前面一个数据的状态不是丢弃状态，那么滑窗内错误数据个数+1
                window_fault_count += 1
 
                if window_fault_count < t:
                    # 如果滑窗内错误数据个数没有超过阈值t，那么可以用前面一个数据代替
                    status[r] = FAULT
                    s[r] = s[r-1]
                else:
                    # 如果滑窗内错误数据个数超过了阈值t，那么 r 位置就是故障开始的位置
                    # 此时 r 位置数据需要被丢弃，此时滑窗中断，需要重置滑窗
                    status[r] = ABORT
                    window_fault_count = 0
 
                    # i 位置就是 故障恢复检查期开始位置
                    i = r + 1
 
                    # 故障恢复检查期内连续正确数据个数
                    recovery_correct_count = 0
 
                    while i < len(s):
                        if check_recovery(i):
                            recovery_correct_count += 1
                            status[i] = RECOVERY_NORMAL
 
                            # 当故障恢复期间，连续正确数据个数达到p，则故障解除
                            if recovery_correct_count == p:
                                break
                        else:
                            recovery_correct_count = 0
                            status[i] = RECOVERY_FAULT
 
                        i += 1
 
                    # i 位置是故障解除的位置，则下一次，我们应该从 i+1 位置开始重新判断，即滑窗的左、右边界都要更新为i+1
                    if i < len(s):
                        l = i + 1
                        r = i  # 这里r没有等于 i+1，是后面有while循环的r+=1
 
        r += 1
 
    # 最后只需要找到 status 数组中最长的连续NORMAL和FAULT即可
    maxLength = 0
    length = 0
 
    for sta in status:
        if sta == NORMAL or sta == FAULT:
            length += 1
        else:
            maxLength = max(maxLength, length)
            length = 0
 
    return max(maxLength, length)
 
 
# 算法调用
print(getResult())