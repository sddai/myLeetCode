'''遇到一个测试用例：
两个全是a的字符串，如果p长度大于等于128就报错。 "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

【原因】原因就是Integer类型在大于128的时候就不能直接用==判断相等了
'''
def findAnagrams( s: str, p: str) ->  [int]:
    n = len(s)
    m = len(p)
    need = defaultdict(int)
    for i in range(m):
        need[p[i]] += 1
    valid = 0  
    left = 0
    right = 0
    window = defaultdict(int)
    k = len(need)
    ans = []
    while right < n:
        c = s[right]
        right += 1
        if c in need:
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        while right - left >= m:
            if valid == k:
                ans.append(left)
            d = s[left]
            left += 1
            if d in need:
                if window[d] == need[d]:   # 不能用>=，因为只有刚好减小到等于所需字符数的时候，再往下减就不符合该字符个数了，这时候才需要valid减一，如果是大于，那么移动left减少一个字符不会导致valid减小（即，窗口移出这个字符，还满足valid）
                # 这里有两件事：1. 删除s[left]之后需要减小valid， 2. window的计数也要减小，1在2之前就可以通过，原因是长度大于128的时候用==判断相等会出错
                    valid -= 1
                window[d] -= 1
                # if window[d] < need[d]:
                #     valid -= 1

    return ans

print(findAnagrams("cbaebabacd", "abc"))