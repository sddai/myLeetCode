from collections import defaultdict
def dfs(root, boss_to_children, seller_to_money):
    for child in boss_to_children[root]:
        dfs(child, boss_to_children, seller_to_money)
        # seller_to_money[root] += int(seller_to_money[child] * 0.15)  # 要注意题目的说法：每100元上交15元，不能直接乘以0.15
        seller_to_money[root] += (seller_to_money[child] // 100 * 15)
    return seller_to_money[root]
    
    
def calc(n, alist):
    boss_to_children = defaultdict(list)
    seller_to_money = defaultdict(int)
    for seller, boss, money in alist:
        boss_to_children[boss].append(seller)
        seller_to_money[seller] += money
    return boss_to_children, seller_to_money

n = 3
alist = [[1, 0, 223], [2, 0, 323], [3, 2, 1203]]
b, s = calc(n, alist)
dfs(0, b, s)
print(s[0])
for key, val in s.items():
    print(key, val)
for key, val in b.items():
    print(key, val)