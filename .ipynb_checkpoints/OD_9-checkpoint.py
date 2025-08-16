'''给定一个数组X和正整数K，请找出使表达式X[i] - x[i +1] ... - X[i + K 1]，结果最接近于数组中位数的下标i，如果有多个i满足条件，请返回最大的i。
其中，数组中位数:长度为N的数组，按照元素的值大小升序排列后，下标为N/2元素的值

补充说明:
1.数组X的元素均为正整数;
2.X的长度n取值范围: 2<= n <= 1000;
3.K大于0且小于数组的大小;
4.i的取值范围: 0 <=i < 1000;
5.题目的排序数组X[N]的中位数是X[N/2].
示例1
输入:
[50,50,2,3],2
输出:
1

说明:
1、中位数为50: [50,50,2,3]升序排序后变成[2,3,50,50]，中位数为下标4/2=2的元素50;
2、计算结果为1: X[50,50,2,3]根据题目计算X[i] - ...- X[i + K- 1]得出三个数
0 (X[0]-X[1]= 50 -50) 、
48 (X[1]-X[2] = 50 -2)
-1 (X[2]-X[3]= 2-3) ，
其中48最接近50，因此返回下标1
'''

def find_index(X, K):
    n = len(X)
    nums = sorted(X)
    m = nums[n // 2]
    left = 0
    right = 0
    exp = X[left]
    for i in range(1, K):
        exp = exp - X[i]
    res = abs(exp - m)
    ans = left
    left += 1
    right += 1
    while left < n and right < n:
        exp = exp - X[left - 1] + X[left] * 2 - X[right]
        # res = abs(exp - m)
        if abs(exp - m) <= res:
            res = abs(exp - m)
            ans = left
        left += 1
        right += 1
    return ans

X = list(map(int, input().split()))
K = int(input().strip())
print(find_index(X, K))