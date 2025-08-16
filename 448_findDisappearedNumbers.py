class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        get_dict = dict()
        ans = []
        for i in range(n):
            get_dict[nums[i]] = True
        for i in range(1, n+1):
            if i in get_dict and get_dict[i] == True:
                continue
            ans.append(i)
        return ans
# 简单题