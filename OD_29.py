def find(n, l, numbers):
    for i in range(n):
        
def calc_avg(numbers, start, end):
    

# CSDN 答案：
'''
def find_best_subseq(num_count, min_len, seq_vals):
    """
    根据给定的数字列表，找到满足条件的子序列。
    """

    sorted_seq = sorted(seq_vals)
    lower_bound = sorted_seq[0]
    upper_bound = sorted_seq[-1]

    result_positions = []

    # 使用二分查找法
    while upper_bound - lower_bound >= upper_bound / 10**10:
        middle_value = (lower_bound + upper_bound) / 2
        check_result = verify_subseq(num_count, min_len, seq_vals, middle_value)
        
        if check_result:
            result_positions = check_result
            lower_bound = middle_value
        else:
            upper_bound = middle_value

    # 对子序列进行排序，找到长度最小的子序列
    result_positions.sort(key=lambda x: (x[1], x[0]))

    return result_positions[0]


def verify_subseq(num_count, min_len, seq_vals, target_avg):
    """
    检查是否存在子序列，其几何平均值大于等于给定值。
    """
    
    product_val = 1
    for idx in range(min_len):
        product_val *= seq_vals[idx] / target_avg

    candidates = []
    
    if product_val >= 1:
        candidates.append([0, min_len])

    prev_product = 1
    min_prev_product = float('inf')
    min_prev_idx = 0

    for idx in range(min_len, num_count):
        product_val *= seq_vals[idx] / target_avg
        prev_product *= seq_vals[idx - min_len] / target_avg

        if prev_product < min_prev_product:
            min_prev_product = prev_product
            min_prev_idx = idx - min_len

        if product_val / min_prev_product >= 1:
            candidates.append([min_prev_idx + 1, idx - min_prev_idx])

    if candidates:
        return candidates

    return None


num_count, min_len = map(int, input().split())
seq_vals = [float(input()) for _ in range(num_count)]

starting_point, subseq_length = find_best_subseq(num_count, min_len, seq_vals)
print(starting_point, subseq_length)
'''
