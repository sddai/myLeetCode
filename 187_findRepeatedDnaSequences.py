# 首先，想到滑动窗口+哈希查重
# 哈希这里可以进一步优化，优化成：滑动哈希
# 即：ACGT定义为0、1、2、3四个数字，十个数字用函数计算成一个四进制的数字，用这个数字哈希（相比直接哈希，效率更高）
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []
        left = 0
        right = 9
        # window = defaultdict(int)
        fingerprint = defaultdict(int)
        ans = []
        while right < n:
            # if s[left:right + 1] in fingerprint:
            #     ans.append(s[left:right + 1])
            fingerprint[s[left:right+1]] += 1
            left += 1
            right += 1
            # print(fingerprint)
            # curr = s[left]
        for word in fingerprint.keys():
            if fingerprint[word] > 1:
                ans.append(word)
        return ans

