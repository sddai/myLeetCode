def mergeSort(a: [int]) -> [int]:
    # def mergeHelper(a: [int], start, end)
    
    start = 0
    end = len(a) -1
    # ans = []   # 
    def helper(a: [int], start: int, end: int) -> [int]:
        # print(start, end)
        # leftside = []
        # rightside = []     # 左右半数组不要初始化！！！
        if start == end:
            return [a[start], ]
        # if start + 1 == end:
        #     if a[start] > a[end]:
        #         a[start], a[end] = a[end], a[start]
        #     return [a[start], a[end]]
        
        elif start < end:
            mid = (end + start) // 2      # 这里十分易错！！！ 取两个数的中点坐标，不要用(end-start)//2，而应该用(end+start)//2 ！！
            leftside = helper(a, start, mid)
            rightside = helper(a, mid + 1, end)
        # print(leftside, rightside)
        
        merged = [] # 这段代码从递归到最里层start==end之后，回溯的过程中每一次都会运行
        # if leftside != None and rightside != None:
        #     merged.append(leftside.pop(0) if leftside[0] < rightside[0] else rightside.pop(0))
        # if leftside != None or rightside != None:
        #     merged.extend(leftside if leftside != None else rightside)
        while leftside and rightside:
            if leftside[0] < rightside[0]:
                merged.append(leftside.pop(0))
            else:
                merged.append(rightside.pop(0))
        merged.extend(rightside if rightside else leftside)
        return merged
    ans = helper(a, start, end)
    return ans


print(mergeSort([5, 2, 9, 17, 7 ]))
print(mergeSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(mergeSort([5, 2, 9, 17, 7, 3, 4, 1, 20]))

'''
出错的地方在于合并的过程写错了：
【写法1】（错）
        merged = [] # 这段代码从递归到最里层start==end之后，回溯的过程中每一次都会运行
        # if leftside != None and rightside != None:
        #     merged.append(leftside.pop(0) if leftside[0] < rightside[0] else rightside.pop(0))
        # if leftside != None or rightside != None:
        #     merged.extend(leftside if leftside != None else rightside)
【写法2】（对）
        while leftside and rightside:
            if leftside[0] < rightside[0]:
                merged.append(leftside.pop(0))
            else:
                merged.append(rightside.pop(0))
        merged.extend(rightside if rightside else leftside)

注意对比这两种写法的流程
写法一其实只合并了一次，因为最外层只有一个if，因此只合并了一个元素就退出了
因此要使用写法2，使用while循环，一直合并直到左右两个子序列为空。

另外需要注意：
这段代码从递归到最里层start==end之后，回溯的过程中每一次都会运行
'''