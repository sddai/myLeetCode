# 注意这类有重复元素的二分法如何判断退出条件
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
                # l = mid
                # r = mid
                # while l - 1 >= 0 and nums[l - 1] == target:   # 超时
                #     l = l - 1
                # while r + 1 <= n - 1 and nums[r + 1] == target:
                #     r = r + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        l = -1 if left >= n or nums[left] != target else left
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
                # l = mid
                # r = mid
                # while l - 1 >= 0 and nums[l - 1] == target:
                #     l = l - 1
                # while r + 1 <= n - 1 and nums[r + 1] == target:
                #     r = r + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        r = -1 if right < 0 or nums[right] != target else right
        return [l, r]
        
        
        # return [left, right] if left <= right else [-1, -1]
        
# 第二次提交
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = self.left_bound(nums, target)
        r = self.right_bound(nums, target)
        return [l, r]
    
    def left_bound(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        # if r < 0 or l >= n or nums[l] != target:
            # return -1
        # return l
        if l < n and nums[l] == target:
            return l
        else:
            return -1

    def right_bound(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] == target:
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
        # if r < 0 or l >= n or nums[r] != target:
        #     return -1
        # return r
        if r >= 0 and nums[r] == target:
            return r
        else:
            return -1