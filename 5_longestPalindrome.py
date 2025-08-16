# 1. 双指针中心扩散法，每次以某一个位置为中心向两边扩散，分奇数和偶数两种情况选出最长的
# 2. 动态规划法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
        longest = 0
        # for i in range(n):
            # for k in range(2, n + 1):
                # j = k - i
        for L in range(2, n + 1):   # L 最长取n，所以这里是n+1
            for i in range(n - L + 1): 
                j = i + L - 1
                if s[i] == s[j]:
                    if j - i >= 2:
                        dp[i][j] = dp[i + 1][j - 1]
                    else:
                        dp[i][j] = True
                else:
                    dp[i][j] = False
        for i in range(n):
            for j in range(i, n):
                if dp[i][j] and j - i + 1 > longest:
                    # longest = j - i + 1 > longest ? j - i + 1 : longest 
                    longest = j - i + 1
                    start = i
                    end = j
        return s[start:end + 1]

# 双指针法：
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        length = 0 
        right = 0
        left = 0
        right2 = 0
        left2 = 0
        for i in range(n):
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            # print(left, right, length)
            if right - left + 1 > length:
                length = right - left + 1
                flag1 = left
        length2 = 0
        for i in range(n):
            left2 = i
            right2 = i + 1
            while left2 >= 0 and right2 < n and s[left2] == s[right2]:
                left2 -= 1
                right2 += 1
            left2 += 1
            right2 -= 1
            if  right2 - left2 + 1 > length2:
                length2 = right2 - left2 + 1
                flag2 = left2
        print(length, length2)
        return s[flag1:(flag1+length)] if length > length2 else s[flag2:(flag2+length2)]


# 动态规划法：
def longestPalindrome(s: str) -> str:
    dp = [[False] * len(s) for _ in range(len(s))]
    max_len = 1
    start = 0
    end = 1
    if(len(s)==1):
        return s
    for i in range(len(s)):
        dp[i][i] = True
    for L in range(2, len(s)+1):
        for i in range(len(s)):
            j = i + L - 1
            if(j>=len(s)):
                continue
            if(s[i] != s[j]):
                dp[i][j] =False
            else:
                # if(j-i>=3):
                #     dp[i][j] == dp[i+1][j-1]
                # else:
                #     dp[i][j] = True
                if(j-i < 3):
                    dp[i][j] = True
                else:
                    dp[i][j] = dp[i+1][j-1]
            # if()
            if max_len < j-i+1 and dp[i][j]:
                max_len = j-i+1
                start = i
                end = j+1

    return s[start:end]



print(longestPalindrome("bb"))