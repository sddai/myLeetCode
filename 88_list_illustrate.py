def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    p1, p2 = 0, 0
    nums_tmp = []
    while p1 < m or p2 < n:
        if p1 == m:
            nums_tmp.append(nums2[p2])
            p2 += 1
        elif p2 == n:
            nums_tmp.append(nums1[p1])
            p1 += 1
        elif nums1[p1] < nums2[p2]:
            nums_tmp.append(nums1[p1])
            p1 += 1
        else: # nums1[p1] > nums2[p2]:
            nums_tmp.append(nums2[p2])
            p2 += 1

    # nums1 = nums_tmp[:]
    nums1[:] = nums_tmp  # 这是由于in-place的要求，所以原地修改nums1
    print("nums1: ", nums1)
    print("nums_tmp: ", nums_tmp)


n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]
merge(n1, 3, n2, 3)