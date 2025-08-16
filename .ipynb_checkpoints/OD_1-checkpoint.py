def find(nums):
    n = len(nums)
    all_product = 1
    for i in nums:
        all_product *= i
    left = 1
    right = all_product
    i = 0
    res = -1
    for i in range(n):
        if i == 0:
            left = 1
            right = all_product / nums[0]
        else:
            left *= nums[i - 1]
            right /= nums[i]
        if left == right:
            res = i
            break
    return res

ans = find([2, 5, 3, 6, 5, 6])
print(ans)