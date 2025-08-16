def separate_string(s: str) -> [int, int]:
    n = len(s)
    preSum = [0] * (n + 1)
    for i in range(1, n + 1):
        preSum[i] = preSum[i - 1] + ord(s[i - 1])
    ans = [0, 0]
    for i in range(n - 1):
        for j in range(i + 1, n):
            segment1 = preSum[i]
            segment2 = preSum[j] - preSum[i + 1]
            segment3 = preSum[n] - preSum[j + 1]
            if segment1 == segment2 and segment2 == segment3:
                ans = [i, j]
    return ans


s = str(input())  
print(separate_string(s))