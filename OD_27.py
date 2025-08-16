from collections import defaultdict

def pali(s: str) -> str:
    count = defaultdict(int)
    for c in s:
        count[c] += 1
    selects = [k for k in count.keys()]
    selects.sort()
    ans = ""
    mid = ""
    for i in range(len(selects)):
        curr = selects[i]
        cnt = count[curr]
        if cnt == 1:
            if not mid: 
                mid = curr
            continue
        elif cnt % 2 == 0:
            ans += curr * (cnt // 2)
        else:
            ans += curr * (cnt // 2)
            if not mid:
                mid = curr
    # res = ans + mid + "".join([ans[i] for i in range(len(ans) - 1, -1, -1)])
    res = ans + mid + ans[::-1]
    return res

s = str(input())
print(pali(s))        