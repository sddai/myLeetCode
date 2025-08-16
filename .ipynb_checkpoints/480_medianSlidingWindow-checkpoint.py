import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # window = nums[0:k]
        n = len(nums)
        window = []
        ans = []
        # for i in range(k):   # 前k个直接排序，不用一个一个插入
            # window = bisect.insort_left(window, nums[i])
        window = nums[0:k]
        window.sort()
        ans.append((window[k//2] + window[(k-1)//2]) / 2.0)
        for i in range(k, n):
            # window = bisect.insort_left(window, nums[i])
            num_to_delete = nums[i-k] # 在nums中，走出window的那个元素就是要被删除掉的，找到它在window中的index，并把这个位置用新进入window的值替换
            index_of_delete = bisect.bisect_left(window, num_to_delete)  #相当于在排好序的window里边二分查找被挤出窗口那个元素的下标，并删掉（pop）
            # window[index_of_delete] = nums[i] # 这么加入不能保证顺序是排好序的
            window.pop(index_of_delete)
            bisect.insort_left(window, nums[i])
            ans.append((window[k//2] + window[(k-1)//2]) / 2.0)
        return ans
