def selectionSort(alist:[int])-> [int]:
    n = len(alist)
    # max_item = 0
    for i in range(n, 0, -1):
        max_item = 0    # 注意每次进入循环之后max_item的序号需要重置为0
        for j in range(i):
            if alist[max_item] < alist[j]:
                max_item = j
        alist[max_item], alist[j] = alist[j], alist[max_item]
    return alist
    
    
print(selectionSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(selectionSort([5, 2, 9, 17, 7, 3, 4, 1, 20]))