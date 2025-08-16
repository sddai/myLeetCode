#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param nums int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def findTriplets(self , nums: List[int]) -> List[List[int]]:
        # write code here
        nums.sort()
        n = len(nums)
        # left = 0
        # right = n - 1
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue # 避免重复元素（1）
            # if i > 1 and nums[i] == nums[i - 1] and nums[i] == nums[i - 2]: continue
            target = -nums[i]
            left = i + 1
            right = n - 1
            while i < left and left < right and right < n:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    if nums[left] == nums[left - 1]:
                        left += 1
                    if nums[right] == nums[right + 1]:
                        right -= 1
        return res
