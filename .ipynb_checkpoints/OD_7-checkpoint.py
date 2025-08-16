def canDivide(n: int, m: int, nums: [int]) -> int:
    preSum = [0] * (n + 1)
    preSum[0] = 0
    preSum[1] = nums[0]
    for i in range(2, n + 1):
        preSum[i] = preSum[i - 1] + nums[i - 1]
    found = False
    for i in range(n):
        if found: break
        for j in range(i, n):
            if found: break
            curr_sum = preSum[j + 1] - preSum[i]
            if curr_sum % m == 0:
                found = True
    return 1 if found else 0
    
    
while True:
    # try:
    n, m = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(canDivide(n, m, nums))
    # except:
    #     break
# n, m = list(map(int, input().split()))
# nums = list(map(int, input().split()))
# n, m = [6, 7]
# nums = [2, 12, 6, 3, 5, 5]
# n, m = [10, 11]
# nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print(canDivide(n, m, nums))