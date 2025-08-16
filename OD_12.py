from collections import defaultdict
def common_num(nums1, nums2):
    n = len(nums1)
    m = len(nums2)
    count_dict1 = defaultdict(int)
    count_dict2 = defaultdict(int)
    for i in range(n):
        count_dict1[nums1[i]] += 1
    for i in range(m):
        count_dict2[nums2[i]] += 1
    ans = defaultdict(list)
    # print(count_dict1, count_dict2)
    for num in count_dict1.keys():
        if num in count_dict2:
            ans[min(count_dict1[num], count_dict2[num])].append(num)
    # print(ans)
    for k in sorted(ans.keys()):
        ans[k].sort()
        N = len(ans[k])
        print(k, end="")
        print(":", end="")
        for i, num in enumerate(ans[k]):
            if i == N - 1:
                print(f"{num}\b")
            else:
                print(f"{num},", end="")
                
# 关于结尾用逗号分割各个结果：【用join和map函数】
# print(f"{k}:{','.join(map(str, sorted(ans[k])))}")
                

nums1 = [5, 3, 6, -8, 0, 11]
nums2 =[2, 8, 8, 8, -1, 15]
common_num(nums1, nums2)
nums1 = [5, 8, 11, 3, 6, 8, 8, -1, 11, 2, 11, 11]
nums2 =[11, 2, 11, 8, 6, 8, 8, -1, 8, 15, 3, -9, 11]
common_num(nums1, nums2)