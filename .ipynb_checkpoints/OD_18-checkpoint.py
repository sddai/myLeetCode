def jump(n, nums):
    num_to_index = dict()
    smallest_sum_index = float("inf")
    ans = None
    for i, num in enumerate(nums):
        target = n - num
        if target in num_to_index:
            curr_index_sum = i + num_to_index[target]
            if smallest_sum_index > curr_index_sum:
                smallest_sum_index = curr_index_sum
                ans = [num, target] if i < num_to_index[target] else [target, num]
        else:
            num_to_index[num] = i
    return ans

n = int(input())
nums = list(map(int, input().split()))
print(jump(n, nums))

# def jump(n, nums):
#     count = dict()
#     for i, num in enumerate(nums):
#         if num not in count:
#             count[num] = (1, i)
#         else:
#             count[num] = (count[num][0] + 1, i)
#     ans = [-1, -1]
#     index_sum = 0
#     for i in range(len(nums)):
#         target = n - nums[i]
#         count[nums[i]][0] -= 1
#         if target in count and count[target] > 0:
#             ans = [nums[i], target]
#             index_sum = i + 
#     return ans