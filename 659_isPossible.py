class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        seq = defaultdict(int)   # seq[i]是前边以i结尾的子序列的个数
        count = defaultdict(int) # count[i]是接下来需要处理的数字的个数
        for i in range(n):
            count[nums[i]] += 1
        # seq[nums[0]] += 1  # seq是字典，不是list，所以不需要考虑下标越界问题
        for i in range(n):
            if count[nums[i]] <= 0:
                continue
            if seq[nums[i] - 1] > 0:
                seq[nums[i]] += 1
                seq[nums[i] - 1] -= 1
                count[nums[i]] -= 1
            else:
                if count[nums[i] + 1] <= 0 or count[nums[i] + 2] <= 0:
                    return False
                count[nums[i]] -= 1
                count[nums[i] + 1] -= 1
                count[nums[i] + 2] -= 1
                seq[nums[i] + 2] += 1
                # seq[nums[i]]
        return True