def binarySearch(alist:[int], item:int)-> int:
    n = len(alist)
    left = 0
    right = n-1
    mid = right // 2
    found = False
    while left<=right and found != True:   #注意判断条件要加上left<=right
        if alist[mid] == item:
            found = True
        elif alist[mid] < item:
            left = mid + 1
            mid = (right+left) // 2    # 这里是+不是-
        elif alist[mid] > item:
            right = mid - 1 
            mid = (right+left) // 2    # 这里是+不是-
    return mid


print(binarySearch([0, 1, 2, 8, 13, 17, 19, 42], 13)) # 4
print(binarySearch([0, 1, 2, 8, 13, 17, 19, 42], 0))  # 0
print(binarySearch([0, 1, 2, 8, 13, 17, 19, 42], 17)) # 5
print(binarySearch([0, 1, 2, 8, 13, 17, 19, 42], 42)) # 7