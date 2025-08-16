from collections import deque, defaultdict
def file_size(m, n, file_systems):
    find = dict()
    children = defaultdict(list)
    for i in file_systems:
        if len(i) == 3:
            id_, size_, child = i[0], i[1], i[2]
            find[id_] = size_
            children[id_].append(child)
        elif len(i) == 2:
            id_, size_  = i[0], i[1] 
            find[id_] = size_
    q = deque([n])
    ans = 0
    while q:
        curr = q.popleft()
        ans += find[curr]
        if curr not in children:
            continue
        for child in children[curr]:
            q.append(child)
    return ans

print(file_size(3, 1, [[3, 15], [1, 20, 2], [2, 10, 3]]))
    