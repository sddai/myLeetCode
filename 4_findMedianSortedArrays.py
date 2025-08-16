def findMedianSortedArrays(nums1, nums2) -> float:
    def getKthElement(k):
        """
        - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
        - 这里的 "/" 表示整除
        - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
        - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
        - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
        - 这样 pivot 本身最大也只能是第 k-1 小的元素
        - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
        - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
        - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
        """
        
        index1, index2 = 0, 0
        while True:
            # 特殊情况
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            # 正常情况
            newIndex1 = min(index1 + k // 2 - 1, m - 1)
            newIndex2 = min(index2 + k // 2 - 1, n - 1)
            pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
            if pivot1 <= pivot2:
                k -= newIndex1 - index1 + 1
                index1 = newIndex1 + 1
            else:
                k -= newIndex2 - index2 + 1
                index2 = newIndex2 + 1
    
    m, n = len(nums1), len(nums2)
    totalLength = m + n
    if totalLength % 2 == 1:
        return getKthElement((totalLength + 1) // 2)
    else:
        return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


nums1 = [1, 3, 5, 9]
nums2 = [2, 3, 6]
print(findMedianSortedArrays(nums1, nums2))

'''
这段代码是一种利用二分查找的方法来寻找两个正序数组的中位数的。它定义了一个内部函数getKthElement，用来找到两个数组中第k小的元素。它的主要思路是将两个数组分成左右两部分，使得左边的元素总数等于k，并且左边的最大值小于等于右边的最小值。这样就可以保证第k小的元素在左右两部分的边界上。具体地，它使用了以下步骤：

定义两个索引index1和index2，分别指向nums1和nums2的起始位置。
在循环中，判断特殊情况，即如果某个数组已经遍历完了，那么直接返回另一个数组中第k小的元素；如果k等于1，那么直接返回两个数组中最小的元素。
在正常情况下，计算新的索引newIndex1和newIndex2，分别为index1 + k // 2 - 1和index2 + k // 2 - 1，并取其中不超过数组长度减一的值。这样可以保证每次划分时至少有一个数组能够排除掉k // 2个元素。
计算两个新索引对应的值pivot1和pivot2，并比较它们。如果pivot1小于等于pivot2，那么说明nums1[index1 … newIndex1]都不可能是第k小的元素，可以将它们排除掉，并更新index1为newIndex1 + 1；同时更新k为k减去排除掉的元素个数。反之亦然。
当循环结束时，就可以得到第k小的元素。
在外部函数中，首先计算出两个数组总长度totalLength，并根据奇偶性判断中位数是单个还是两个元素平均值。然后调用内部函数getKthElement来找到相应位置上的元素并返回。

这种方法可以保证每次循环都能够排除掉至少一个数组中k // 2个元素，因此时间复杂度为O(log(m + n))；空间复杂度为O(1)，因为只需要常数级别额外空间。
'''
