'''
使用二分法，不断缩小车辆容量的范围，直到找到最小的车辆容量。
对于每个潜在的车辆容量，调用can_transport函数，判断是否能够运输所有的货物。
can_transport函数的逻辑是，根据货物的类型，分配干货车和湿货车，检查是否超过了车辆的限制。
'''
def min_cap(length, goods, types, k):
    
    