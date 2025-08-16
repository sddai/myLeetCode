# 此题的本质是维护一个定长的滑动窗口
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        left = 0
        right = 0
        count_char_in_window = defaultdict(int)
        needed = defaultdict(int)
        valid = 0
        # ans = False
        for i in range(n1):
            needed[s1[i]] += 1
        while right < n2:
            if s2[right] in needed:
                count_char_in_window[s2[right]] += 1
                if count_char_in_window[s2[right]] == needed[s2[right]]:
                    valid += 1
            right += 1
            # while right - left >= n1:   # 【注意】这里有两种情况需要处理：如果长度相等，就判断是否满足排列关系，如果取大于号，则一定是false
            if right - left >= n1:     # while, if 都能过，且也可写成等号——>  if right - left == n1:    
                if len(needed) == valid:
                    return True
                if s2[left] in needed:
                    if count_char_in_window[s2[left]] == needed[s2[left]]:
                        valid -= 1
                    count_char_in_window[s2[left]] -= 1
                left += 1
        return False
