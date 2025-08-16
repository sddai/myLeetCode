from collections import defaultdict, deque
import heapq
def priority_queue(alist):
    q = []
    priorityToVal = dict()
    priorityTest = defaultdict(set)
    for num, priority in alist:
        heapq.heappush(q, -priority)
        if priority not in priorityTest:
            priorityToVal[priority] = deque([num])
            priorityTest[priority].add(num)
        elif num in priorityTest[priority]:
            continue
        elif num not in priorityTest[priority]:
            priorityToVal[priority].append(num)
    ans = []
    while q:
        curr_priority = - heapq.heappop(q)
        while priorityToVal[curr_priority]:
            ans.append(priorityToVal[curr_priority].popleft())
    return ans

X = [[10, 1], [20, 1], [30, 2], [40, 3]]
X = [[10, 1], [10, 1], [30, 2], [40, 3]]
print(priority_queue(X))


'''参考答案:
def ordered_priority_queue(tasks):
    # 创建一个字典用于收集具有相同优先级的数据。
    # 字典的键是优先级，值是一个集合，用于去重并保持插入顺序。
    data_map = {}

    # 遍历每一个任务
    for num, priority in tasks:
        # 如果优先级不在字典中，我们初始化它为一个空集合。
        if priority not in data_map:
            data_map[priority] = set()

        # 添加数字到相应的优先级集合中。
        data_map[priority].add(num)

    # 初始化一个列表来保存结果。
    result = []

    # 按照优先级降序排列，并遍历
    for priority in sorted(data_map.keys(), reverse=True):
        # 添加数字到结果中，注意集合是无序的，但我们是按照插入顺序来添加的。
        result.extend(data_map[priority])

    return result

tasks = [(10,1),(20,1),(30,2),(40,3)]
print(ordered_priority_queue(tasks))  # 输出：[40, 30, 10, 20]

tasks = [(10,1),(10,1),(30,2),(40,3)]
print(ordered_priority_queue(tasks))  # 输出：[40, 30, 10]

'''