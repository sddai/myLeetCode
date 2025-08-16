def data_center(n, positions):
    positions.sort(key = lambda x: (x[0], x[1]))
    acc = 0.5
    tmp = []
    for x, y in positions:
        tmp.append(x)
        tmp.append(y)
    tmp.sort()
    left = tmp[0]
    right = tmp[-1]
    while right - left > acc:
        k = (right - left) / 3
        mid_l = left + k
        mid_r = right - k
        distance_l = 0
        distance_r = 0
        for i in range(n):
            start, end = positions[i]
            if end < mid_l:
                distance_l += mid_l - end
            elif start > mid_l:
                distance_l += start - mid_l
            else:
                distance_l += 0
            if end < mid_r:
                distance_r += mid_r - end
            elif start > mid_r:
                distance_r += start - mid_r
            else:
                distance_r += 0 
        if distance_l <= distance_r:
            right = mid_r
        elif  distance_l > distance_r:
            left = mid_l
    return int(distance_r)

n = int(input())
positions = []
for i in range(n):
    left, right = list(map(int, input().split()))
    positions.append([left, right])
print(data_center(n, positions))        
        