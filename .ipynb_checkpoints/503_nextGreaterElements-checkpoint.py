class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums[0:n-1])
        m = len(nums)
        stack = []
        nextLarger = [-1 for _ in range(m)]
        # cnt = 0
        for i in range(m):
            # cnt += 1
            while stack and nums[stack[-1]] < nums[i]:
                nextLarger[stack[-1]] = nums[i]
                stack.pop()
            stack.append(i)
            # if i == n-1:
            #     i = 0
        return nextLarger[0:n]
# 单调栈

# 循环数组的另一种处理方法：
# 在本题中，我们不需要显性地将该循环数组「拉直」，而只需要在处理时对下标取模即可。
        # for i in range(n * 2 - 1):
        #     while stk and nums[stk[-1]] < nums[i % n]:
        #         ret[stk.pop()] = nums[i % n]
        #     stk.append(i % n)

# 第二次通过
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [0]
        n = len(nums)
        i = 1
        cnt = 1
        res = [-1] * n
        while cnt <= 2 * n - 1:
            if i == n:
                i = 0
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                res[idx] = nums[i]
            # else:  # 这里不是else的关系，而是都加入stack的关系
                # stack.append(i)
            stack.append(i)
            i +=1 
            cnt += 1
        return res