def count_car(nums, size):
    n = len(nums)
    color_count = {0: 0, 1: 0, 2: 0}
    left = 0
    right = 0
    ans = 0
    while left < n and right < n:
        if left < n and right < n and right - left + 1 > size:
            color_count[nums[left]] -= 1
            left += 1
            # right += 1
        elif left < n and right < n:
            color_count[nums[right]] += 1
            right += 1
        for k,v in color_count.items():
            ans = max(ans, v)
    return ans

nums = list(map(int, input().split()))
size = int(input())
print(count_car(nums, size))