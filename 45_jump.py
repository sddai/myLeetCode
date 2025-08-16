# 这里解释贪心算法的可行性：
# 是否有一种可能，本轮跳到i，但是nums[i]+i要比nums[i-1]+i-1的值小，也就是说，从上一步跳出去的位置更远？
# 是没有可能的，因为，数组逐渐更新（i递增），如果到第i-1步跳的更远，那么max_reach在i-1步就应该更新为那个最大值，第i步不更新max_reach
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        max_reach = 0
        steps = 0
        end = 0
        for i in range(n-1):   # i = 0 ... n-2 ，这是由于，开始的时候边界是第 0 个位置，steps 已经加 1 了。如下图，如果最后一步刚好跳到了末尾，此时 steps 其实不用加 1 了。如果是 i < n，i 遍历到最后的时候，会进入 if 语句中，steps 会多加 1
            if max_reach >= i:
                max_reach = max(max_reach, nums[i] + i)
                print(max_reach)
                if i == end:   # 用 end 表示当前能跳的边界,遇到边界，就更新边界，并且步数加一（注意这里更新的边界是这一步覆盖到的所有点能达到的最远处）
                    end = max_reach
                    steps += 1
        return steps
    
# 【第二次一遍通过】
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        max_end = 0
        temp_end = 0
        jump = 0
        while i < n:
            while i <= max_end:
                temp_end = max(temp_end, nums[i] + i)
                i += 1
            max_end = temp_end
            jump += 1
            if max_end >= n - 1:
                return jump