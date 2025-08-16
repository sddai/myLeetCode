from collections import deque


def hotPotato(num: int, kill: int) -> int:
    queue = deque(range(1, num+1))
    count = 0
    while True:
        curr = queue.popleft()
        # print(curr, end=" ")
        # print("count=", count)
        count += 1
        if count == kill:   
            count = 0
            print(curr, end=" ")
            
        else:
            queue.append(curr)
        if len(queue) == 1:
            break
    return queue.popleft()


print("ans: ", hotPotato(40, 7))


def josephus(n, k):
    # 创建一个包含n个人的deque，每个人用一个编号表示
    d = deque(range(1, n + 1))
    # 当deque中还有多于一个人时，循环执行
    while len(d) > 1:
        # 将deque中的元素向左循环移动k-1步，使得第k个人在右端
        d.rotate(-(k - 1))
        # 从右端弹出并打印第k个人的编号，表示淘汰
        print(d.pop(), end=" ")
        # d.pop()
    # 返回deque中剩下的最后一个人的编号，表示胜利
    return d[0]

# 测试
print("ans:", josephus(40, 8))