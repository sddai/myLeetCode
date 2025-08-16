# 【总体思路】：先通过递增右指针（扩大窗口），找到【可行解】，然后通过递增左指针（缩小窗口）找到最优解
# 1、左右指针，初始化 left = right = 0，把索引左闭右开区间 [left, right) 称为一个「窗口」。
# 2、我们先不断地增加 right 指针扩大窗口 [left, right)，直到窗口中的字符串符合要求（包含了 T 中的所有字符）。
# 3、此时，我们停止增加 right，转而不断增加 left 指针缩小窗口 [left, right)，直到窗口中的字符串不再符合要求（不包含 T 中的所有字符了）。同时，每次增加 left，我们都要更新一轮结果。
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        left = 0
        right = 0
        count_in_window = defaultdict(int)
        needed = defaultdict(int)
        count_valid_char = 0
        start = 0
        length = float("inf")  # 由于题目要求长度最小，所以用一个变量来记录当前有效子串的长度
        for i in range(m):
            needed[t[i]] += 1
        while right < n:
            if s[right] in needed: 
                count_in_window[s[right]] += 1
                if count_in_window[s[right]] == needed[s[right]]:
                    # end = right
                    count_valid_char += 1
            right += 1
            # 【注意】这里的区间是左闭右开的，right是取不到的，所以right是有效子串的下一个元素
            while count_valid_char == len(needed):
                if right - left < length:
                    start = left  # 这里一起更新start和length
                    length = right - left
                if s[left] in needed:  # s[left]就是下一个要移出窗口的元素
                    if count_in_window[s[left]] == needed[s[left]]: # 注意if和下一句减少计数之间的顺序：如果当前恰好刚好满足需要的字符个数，则继续缩减窗口会导致valid的个数少一，然后再移动窗口
                        count_valid_char -= 1
                    count_in_window[s[left]] -= 1
                left += 1
                # if count_valid_char >= len(needed): # 这段不需要
                #     start = left
                #     left += 1

        return s[start:start+length] if length != float("inf") else ""

# 第二次提交：
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        need = defaultdict(int)
        count_c_in_window = defaultdict(int)
        n = len(s)
        m = len(t)
        valid = 0
        for i in range(m):
            need[t[i]] += 1
        # required = len(need.keys())
        window_length = float("inf")
        start = 0
        while right < n:
            c = s[right]
            right += 1   # 注意窗口达到满足条件之后right在下一个位置，所以是左闭右开区间
            # if valid < required:   # 这部分是扩大窗口的过程，但是valid==req的时候也可以扩大窗口
                # c = s[right]
            # if need[c]:
            if c in need:   # 【思考】if c in need 和 if need[c] 的区别：need[c]原来不为零，但是通过收缩窗口变成0，这时候need[c]==False但是c in need==True
                count_c_in_window[c] += 1
                if count_c_in_window[c] == need[c]:
                    valid += 1 
            
            # if valid == required:
            # 接下来是收缩窗口的过程，收缩过程是while循环，while valid < len(need):
            # else:
            while valid == len(need):
                # if window_length > right - left + 1:
                if window_length > right - left:  # 左闭右开
                    window_length = right - left
                    start = left
                d = s[left]
                left += 1
                # if count_c_in_window[c]:   # 注意这里对移出窗口的处理
                #     count_c_in_window[c] -= 1
                # if count_c_in_window[c] < need[c]:
                #         valid -= 1
                if d in need:
                    if count_c_in_window[d] == need[d]:
                        valid -= 1
                    count_c_in_window[d] -= 1
                    # if count_c_in_window[d] == need[d] - 1:
                    #     valid -= 1
                
        return s[start:(start+window_length)] if window_length < float("inf") else ""
        # if len(s[left:(left+window_length)]) == m else ""              
