def shellSort(a: [int]) -> [int]:
    def insertionSort(a: [int], start: int, gap: int) -> [int]:
        for i in range(start+gap, n, gap):
            for j in range(i-gap, -1, -gap):
                if a[j] > a[j+gap]:
                    a[j], a[j+gap] = a[j+gap], a[j]
    n = len(a)
    gap = n // 2
    while gap >= 1:
        for start in range(gap):
            insertionSort(a, start, gap)
        gap = gap // 2

    return a
                
  
print(shellSort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
print(shellSort([5, 2, 9, 17, 7, 3, 4, 1, 20]))