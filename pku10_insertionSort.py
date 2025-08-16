def insertionSort(alist: [int]) -> [int]:
    n = len(alist)
    for i in range(1, n):
        currNum = alist[i]
        for j in range(i-1, -1, -1):
            if alist[j] > currNum:
                alist[j+1], alist[j]= alist[j], alist[j+1]
            else:
                # alist[j] = currNum
                break
    return alist


def insertionSort2(alist: [int]) -> [int]:
    n = len(alist)
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if alist[j] > alist[j+1]:
                alist[j+1], alist[j] = alist[j], alist[j+1]
    return alist
            
            
def insertionSort_bak(alist: [int]) -> [int]:
    n = len(alist)
    for i in range(1, n):
        currNum = alist[i]
        # print("curr = ", currNum)
        for j in range(i-1, -1, -1):
        # for j in range(i+1, 1, -1)
            # print("alist[j] = ", alist[j])
            if alist[j] > currNum:
                alist[j+1], alist[j] = alist[j], alist[j+1]
                # alist[j+1] = alist[j]
                # print("交换")
            # else:        # 这个else写错了，应该在内层循环之外
                # alist[j+1] = currNum
            # else:
            #     print("j in else, ", j)
            #     alist[j+1] = currNum
        # alist[j] = currNum #################### 去掉这句就正确了，最后不需要重新赋值alist[j]，因为前边是交换的
                # print("结束内层循环")
                # break
        # print("alist[j]=currNum")
        # alist[j] = currNum
    return alist
    

print(insertionSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(insertionSort_bak([5, 2, 9, 17, 7, 3, 4, 1, 20]))
print(insertionSort([5, 2, 9, 17, 7, 3, 4, 1, 20]))
print("========")
print(insertionSort2([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(insertionSort2([5, 2, 9, 17, 7, 3, 4, 1, 20]))
print(insertionSort2([5, 2, 9, 17, 7, 3, 4, 1, 20]))
# print([i for i in range(2, 0, -1)])   # 注意range(2, 0, -1)的结果是[2, 1]，而不是[1, 0]
# print([i for i in range(4, -1, -1)])   # range(4, -1, -1)结果是[4, 3, 2, 1, 0]