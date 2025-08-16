from math import sqrt
import heapq


def get_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def get_center(alist):
    n = len(alist)
    sum_x = 0
    sum_y = 0
    # print(alist)
    for x, y in alist:
        sum_x += x
        sum_y += y
    return [sum_x / n, sum_y / n]
    
    
def kmeans(datacenters, users, m):
    n = len(datacenters)
    count_users = len(users)
    curr_center = datacenters[:]
    curr_x = 0
    curr_y = 0
    q = []
    for i in range(m):
        # curr_center = 
        for x, y in curr_center:
            # curr_x = x
            # curr_y = y
            curr_dist = 0
            for point_x, point_y in users:
                # curr_x += point_x
                # curr_y += point_y
                # curr_dist += get_distance(x, y, point_x, point_y) 
                
            # new_x = curr_x / 
            # tmp.append(curr_dist)
            heapq.heappush(q, (curr_dist, [x, y]))
        tmp = []
        for i in range(len(q)):
            dist, point = heapq.heappop(q)
            # alist = point.extend(users)
            alist = [point, ]
            alist.extend(users)
            new_x, new_y = get_center(alist)
            tmp.append([new_x, new_y])
        # print(tmp)
        curr_center = tmp[:]
        q = []
    return curr_center
            
            
dc = [[114.0, 86.0], [116.0,84.0]]
users = [[119.37,81.03], [119.73,79.51],[121.51,81.29],[120.17,79.14],[119.7,79.64],[111.49,90.02],[109.66,91.63],[110.27,89.6],[110.36,88.7],[110.87,89.50]]
m = 3
print(kmeans(dc, users, m))

