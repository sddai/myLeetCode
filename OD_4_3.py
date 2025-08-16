def longest_continuous_period(m, t, p, samples):
    def is_valid_sample(curr, prev):
        if curr <= 0 or curr < prev or curr - prev >= 10:
            return False
        return True

    n = len(samples)
    errors_in_window = 0
    max_len, curr_len = 0, 0
    prev_valid_sample = -1  # 初始值

    for i in range(n):
        if i > 0 and is_valid_sample(samples[i], samples[i-1]):
            curr_len += 1
        else:
            if prev_valid_sample == -1:
                curr_len = 0
            else:
                samples[i] = prev_valid_sample
                errors_in_window += 1
                curr_len += 1
                
        if i >= m:
            if samples[i-m] != prev_valid_sample:
                errors_in_window -= 1
        
        if errors_in_window == t:
            curr_len -= m
            errors_in_window = 0
        
        if curr_len > max_len:
            max_len = curr_len
        
        if is_valid_sample(samples[i], samples[i-1] if i > 0 else -1):
            prev_valid_sample = samples[i]

    return max_len


# m, t, p = map(int, input().split())
# samples = list(map(int, input().split()))
m, t, p = [10, 6, 3]
samples = [-1, 1, 2, 3, 100, 13, 9, 10]
print(longest_continuous_period(m, t, p, samples))


'''from collections import deque

def takeSampleFilter(M, T, P, samples):
    i = 0
    n = len(samples)
    cycle = 0
    fail = 0
    sampleDeque = deque()  # 使用双端队列保存正常数据的下标

    while i < n:
        if cycle <= M:  # 判断是否满足连续周期条件
            if fail == T:  # 判断是否达到连续失败条件
                count = P
                while count > 0 and i < n:
                    if judge(samples, i):  # 判断当前样本数据是否为正常值
                        count = P
                    else:
                        count -= 1
                    i += 1
                cycle = fail = 0  # 重置连续周期数和连续失败数
                continue
            if cycle == M:  # 如果连续周期数达到上限，需要重置
                cycle = fail = 0
                continue

        if judge(samples, i):  # 判断当前样本数据是否为正常值
            fail += 1
            if sampleDeque:
                samples[i] = samples[sampleDeque[-1]]  # 使用最近一个正常值代替错误值
                sampleDeque.append(i)
        else:
            sampleDeque.append(i)

        cycle += 1
        i += 1

    ans = 0
    lastIndex = sampleDeque.pop()  # 取出最后一个正常值的下标
    temp = 1
    while sampleDeque:
        if sampleDeque[-1] + 1 == lastIndex:  # 判断当前下标是否与上一个下标相邻
            temp += 1
            lastIndex = sampleDeque.pop()  # 取出下一个正常值的下标
        else:
            ans = max(ans, temp)  # 更新最长连续周期数
            lastIndex = sampleDeque.pop()  # 取出下一个正常值的下标
            temp = 1

    return temp if ans == 0 else ans

def judge(samples, i):
    return samples[i] <= 0 or (i >= 1 and (samples[i] < samples[i-1])) or samples[i] - samples[i-1] >= 10

# 读取输入
# M, T, P = map(int, input().split())
# samples = list(map(int, input().split()))
M, T, P = [10, 6, 3]
samples = [-1, 1, 2, 3, 100, 13, 9, 10]

# 计算正常值的最长连续周期
result = takeSampleFilter(M, T, P, samples)

# 输出结果
print(result)
'''

# def longest_continuous_period(m, t, p, samples):
#     def is_valid_sample(curr, prev):
#         if curr <= 0 or curr < prev or curr - prev >= 10:
#             return False
#         return True

#     n = len(samples)
#     errors_in_window = 0  # 滑窗内错误数
#     max_len, curr_len = 0, 0
#     prev_valid_sample = -1 

#     for i in range(n):
#         if i > 0 and is_valid_sample(samples[i], samples[i-1]): # i=1及其之后的元素，有效的
#             curr_len += 1   # 当前有效长度+=1
#         else:    # 
#             if prev_valid_sample == -1:
#                 curr_len = 0   # 处理第i=0个元素无效的情况
#             else:  # 第1个及以后的无效元素：
#                 samples[i] = prev_valid_sample   # 有错误，先恢复错误，curr_len继续计数
#                 errors_in_window += 1
#                 curr_len += 1 
                
#         if i >= m:
#             if samples[i-m] != prev_valid_sample:   # 如果被滑出窗口之外的那个元素不等于prev_valid_sample，那么说明这个元素是被纠正过的
#                 errors_in_window -= 1
        
#         if errors_in_window == t:  # 已经触发故障周期
#             curr_len -= m
#             errors_in_window = 0
        
#         if curr_len > max_len:
#             max_len = curr_len
        
#         if is_valid_sample(samples[i], samples[i-1] if i > 0 else -1):
#             prev_valid_sample = samples[i]  # 前一个有效元素

#     return max_len


# m, t, p = map(int, input().split())   # fault_window_size, fault_thresh, restore_time
# samples = list(map(int, input().split()))
# print(longest_continuous_period(m, t, p, samples))
