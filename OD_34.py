def money(n, nums):
    stack = []
    stack.append(0)
    right_larger = [-1] * n
    ans = [-1] * n
    for i in range(1, n):
        while stack and nums[stack[-1]] <= nums[i]:
            index = stack.pop()
            right_larger[index] = i
        stack.append(i)
    for i in range(n):
        if right_larger[i] == -1:
            ans[i] = nums[i]
        else:
            ans[i] = (nums[right_larger[i]] - nums[i]) * (right_larger[i] - i)
    return ans

print(money(3, [2, 10, 3]))
    