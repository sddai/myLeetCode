def bubbleSort(alist: [int])-> [int]:
    n = len(alist)
    for i in range(n-1, 0, -1):     # 注意这里外层循环是倒序的
        for j in range(i):
            if alist[j] > alist[j+1]:
                # alist[j], alist[j+1] = alist[j+1], alist[j]
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp
    return alist

print(bubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))