from collections import defaultdict
from math import sqrt

# N~20：回溯
def dfs( start, nums, n, used):
    ans = 0
    for i in range(start, n):
        # if not used[i]:
        #     a = nums[i]
        if used[i]: continue
        for j in range(i + 1, n):
            # if not used[j]:
            #     b = nums[j]
            if used[j]: continue
            for k in range(j + 1, n):
                # if not used[k]:
                #     c = nums[k]
                if used[k]: continue
                if nums[i] ** 2 + nums[j] ** 2 == nums[k] ** 2:
                    used[i] = True
                    used[j] = True
                    used[k] = True
                    ans = max(ans, 1 + dfs( start + 1, nums, n, used))
                    used[i] = False
                    used[j] = False
                    used[k] = False
    return ans
                        
                    

def triangle(n, nums):
    used = [False] * n
    # ans = 0
    nums.sort()
    res = dfs( 0, nums, n, used)
    return res
    # for i in range(n)


T = int(input())
for i in range(T):
    line = list(map(int, input().split()))
    n = line[0]
    nums = line[1::]
    print(triangle(n, nums))

    
    
# def isValid(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     else:
#         return False
    
    
# def triangle(n, nums):
#     nums.sort()
#     count = defaultdict(int)
#     for num in nums:
#         count[num] += 1
#     ans = 0
#     for i in range(n - 2):
#         a = nums[i]
#         for j in range(i + 1, n - 1):
#             b = nums[j]
#             c = sqrt(a ** 2 + b ** 2)
#             if c in count and isValid(a, b, c):
#                 ans += 1
#     return ans