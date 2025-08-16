# 约瑟夫环的变体：注意还要求数字里边含有7
def sort_Yuesefu(nums):
    K = 7
    n = len(nums)
    total = sum(nums)
    count = 0
    ans = [0] * n
    # index = K
    i= 0
    while count < total:
        # ans[index - 1] += 1
        # count += 1
        # index = (index + K) % n
        # if (i + 1) % K == 0 or str(K) in set(c for c in str(nums[i % n])):
        # if (i + 1) % K == 0 or str(K) in str(nums[i % n]):  # 注意这里不对，最后需要寻找里边有没有7的应该是i+1，而不是nums[i%n]
        if (i + 1) % K == 0 or str(K) in str(i+1):
            ans[i % n] += 1
            count += 1
        i += 1
    return ans

nums = list(map(int, input().split()))
result = sort_Yuesefu(nums)
print(" ".join(str(i) for i in result))