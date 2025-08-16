from collections import defaultdict
def max_reliability(s, n, total, alist):
    # 目标：在不超预算的条件下，尽可能使【最小可靠性最大】
    # 因此，这是一个典型的二分法问题
    # 要找的函数就是: 花费=f() 是否满足f(reliability)不超预算  -> 变换思路：对于每一种可能的reliability，check他是否满足预算约束条件（逐个试）
    # alist.sort(key = lambda x: x[1])
    get_relia_and_price = defaultdict(list)
    size_of_type = [0] * n
    all_relias = set()
    for type_, reliability, price in alist:
        get_relia_and_price[type_].append([reliability, price])   
        size_of_type[type_] += 1
        all_relias.add(reliability)
    for i in range(n):
        get_relia_and_price[i].sort()
    search_relias = sorted(list(all_relias))
    ans = bisearch(s, n, search_relias, get_relia_and_price, size_of_type)
    return ans
    
def bisearch(s, n, search_relias, get_relia_and_price, size_of_type):
    l = 0
    r = len(search_relias) - 1
    opt = -1
    while l <= r:
        mid = l + (r - l) // 2  
        result = check_price(s, n, search_relias[mid], search_relias, get_relia_and_price, size_of_type)
        if result:
            opt = search_relias[mid] 
            # r = mid - 1
            l = mid + 1    # 如果当前这个可靠度满足价格约束，那么，搜索更大的可靠度
        else:
            # l = mid + 1
            r = mid - 1   # 如果当前这个relia不满足价格约束，说明太高了，向左移动搜索区间
    return opt
        
def check_price(s, n, reliability, search_relias, get_relia_and_price, size_of_type):
    total_price = 0
    # print(size_of_type, get_relia_and_price)
    for i in range(n):
        l = 0
        r = size_of_type[i] - 1
        # pos = -1
        while l <= r and l <= size_of_type[i] - 1 and r >= 0:
            mid = l + (r - l) // 2
            # print(l, mid, r)
            # print([get_relia_and_price[i][j][0] for j in range(size_of_type[i])])
            # print(reliability)
            curr_relia = get_relia_and_price[i][mid][0]
            if curr_relia < reliability:
                l = mid + 1
            elif curr_relia > reliability:
                # pos = mid
                r = mid - 1
            else:
                # pos = mid
                r = mid - 1         
        # total_price += get_relia_and_price[i][l][1] if l < size_of_type[i] else get_relia_and_price[i][size_of_type[i] - 1][1]
        # 【注意】left总是指向第一个大于target的数字，或者不存在大于target的数字，此时left == n
        # print(pos)
        # total_price += get_relia_and_price[i][pos][1]
        if l >= 0 and l <= size_of_type[i] - 1:
            total_price += get_relia_and_price[i][l][1]
        else:   # 这种情况下，说明最大的一个reliability也不满足条件，return False
            # total_price += get_relia_and_price[i][l - 1][1]
            return False
    return total_price <= s
    
'''
def check_price(s, n, reliability, search_relias, get_relia_and_price, size_of_type):
    total_price = 0
    # found = False  # 注意每次进入循环都要重置flag
    for i in range(n):
        found = False
        # index = bisearch()  # 不用套bisearch
        for relia, price in get_relia_and_price[i]:   # 这里可以优化：将逐个寻找换成二分查找
            if relia >= reliability:
                total_price += price
                found = True
                break
        if not found:
            return False
    return total_price <= s
'''


s = 500
n = 3
total = 6
alist = [[0, 80, 100], [0, 90, 200], [1, 50, 50], [1, 70, 210], [2, 50, 100], [2, 60, 150]]
print(max_reliability(s, n, total, alist))

s = 100
n = 1
total = 1
alist = [[0, 90, 200]]
print(max_reliability(s, n, total, alist))