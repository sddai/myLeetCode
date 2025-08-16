class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # left = 0   
        # 左右指针求出来的是cap，是子数组中数字之和，所以cap最小是nums里边最大那个元素的值，最大是所有之和
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            m = self.find_m(mid, nums)
            if m < k:
                right = mid - 1
            elif m == k:
                right = mid - 1   # 找左边界
            elif m > k:
                left = mid + 1
        return left
        
    def find_m(self, cap, nums):
        # cap是每个连续子数组的最大和上限（容量）
        # 返回对应的m
        n = len(nums)
        sub_arr_sum = 0
        m = 1
        # i = 0
        for num in nums:
            if sub_arr_sum + num > cap:
                m += 1
                sub_arr_sum = num
            else:
                sub_arr_sum += num
        # while i < n:
        #     while i < n and sub_arr_sum + nums[i] <= cap:
        #         sub_arr_sum += nums[i]
        #         i += 1
        #     m += 1
        #     sub_arr_sum = nums[i]
        #     i += 1
        return m