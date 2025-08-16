class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        m = len(nums2)
        ans_temp = [-1 for _ in range(m)]
        ans = [-1 for _ in range(n)]
        get_index = dict()
        stack = []
        for idx, item in enumerate(nums2):
            get_index[item] = idx
        for i in range(m):
            while stack and nums2[i] > nums2[stack[-1]]:
                # j = get_index[nums1[stack[-1]]]   # 
                ans_temp[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i)
        for i in range(n):
            j = get_index[nums1[i]]
            ans[i] = ans_temp[j]
        return ans
# 单调栈