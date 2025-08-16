# 此题第二遍一次通过
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        window = set()
        length = 0
        while right < n:
            c = s[right]
            while c in window:
                d = s[left]
                window.remove(d)
                left += 1
            else:
                window.add(c)
                right += 1
            if right - left > length:
                length = right - left
        return length


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        char_set = dict()
        max_length = 0
        left = 0
        for i in range(length):
            
            if s[i] in char_set and char_set[s[i]]>=left:
                left = char_set[s[i]] + 1   # char_set[s[i]不能用i替代，因为i是第二个出现的当前字符，需要的是第一次出现的位置
            # else:
                # max_length += 1
            char_set[s[i]] = i 
            # char_set[s[i]] = i 这句要放在if判断之后，原因是要在元素加入字典之前就判断之前有没有重复元素，否则，如果if之前就把元素加进字典，那么if判断一定有重复
            max_length = max(max_length, i - left +1)
        return max_length


# def lengthOfLongestSubstring(s):
#     # 初始化一个空字典，用来存储字符和索引的映射
#     dic = {}
#     # 初始化最大长度为0
#     max_len = 0
#     # 初始化滑动窗口的左边界为0
#     left = 0
#     # 遍历字符串中的每个字符
#     for i in range(len(s)):
#         # 如果当前字符已经在字典中出现过，并且出现的位置不小于左边界
#         if s[i] in dic and dic[s[i]] >= left:
#             # 更新左边界为该字符上次出现位置的下一位
#             left = dic[s[i]] + 1
#         # 否则，更新最大长度为当前长度和之前最大长度中的较大值
#         else:
#             max_len = max(max_len, i - left + 1)
#         # 更新字典中当前字符的索引值为i
#         dic[s[i]] = i
#     # 返回最大长度
#     return max_len

# # 测试代码：
# s = "abcabcbb"
# print(lengthOfLongestSubstring(s)) # 输出3

"""
这段代码的思路是：

首先创建一个空字典，用来存储每个字符在字符串中最后出现的位置。
然后初始化一个变量max_len，用来记录最长不重复子串的长度。
接着初始化一个变量left，用来表示滑动窗口的左边界。
接下来遍历字符串中的每个字符，对于每个字符：
如果它已经在字典中出现过，并且它上次出现的位置不小于left，说明它和当前滑动窗口内的某个字符重复了，那么就需要把left移动到它上次出现位置的下一位，相当于把重复字符从滑动窗口中排除掉。
否则，说明它没有和当前滑动窗口内的任何字符重复，那么就可以更新max_len为当前滑动窗口内子串的长度和之前记录的max_len中较大者。
最后更新字典中该字符对应的索引值为当前遍历到的位置i。
最终返回max_len即可。
这段代码使用了O(n)时间复杂度和O(1)空间复杂度（因为字典中最多只有26个英文字母）。

这段代码已经很简洁高效了，但是如果你想进一步优化，你可以参考一些网上的建议123：

你可以使用Python的yield关键字来实现滑动窗口的生成器，这样可以节省内存空间，提高运行速度。yield可以让函数返回一个可迭代对象，每次调用时只返回一个值，而不是一次性返回所有值。12
你可以使用Python的内置函数和模块来替换一些自己写的循环或判断语句，比如使用collections.Counter来统计字符出现的频率，或者使用itertools.groupby来分组相同的字符。这样可以减少代码量，提高可读性和效率。3
你可以使用Python的多线程或多进程来并行处理数据，利用CPU的多核特性来加速运算。但是需要注意线程安全和进程间通信的问题。3
"""