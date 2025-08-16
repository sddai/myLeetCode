# 【思路】使用队首维护最大值, 队尾加入待选值 -> 这就是一个单调队列
# 使用本题方法，维护的队列，能保证最大值就是queue[0]
# 因为，遇到比前边值大的数，会把所有小的都出队列，比前边小的数，会直接附在后边
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        ans = []
        if not nums or not k:
            return []
        if n == 1:
            return nums

        for i in range(n):
            # 注意如何判断队列满：
            # if len(q) == k:  # 不对
            if q and q[0] == i - k:
                q.popleft() 
            if i < k-1:
                # while q and nums[q[0]] < nums[i]:
                while q and nums[q[-1]] < nums[i]:
                    q.pop()
                q.append(i)
                # print(q)
                # ans.append(nums[q[0]]) # 前k个不需要输出到ans
            else:
                # while q and nums[q[0]] < nums[i]:  # 这里不对，由于是一个单调队列，所以应该是后边的小，要从q[-1]开始逐个把原来元素删掉
                while q and nums[q[-1]] < nums[i]:
                    q.pop()
                q.append(i)
                # while len(q) > k: # 不要在这里判断队列满
                #     q.popleft()
                # print(q)
                ans.append(nums[q[0]])
        return ans        
                 
# 第二次提交
# 单调递减栈：
# 1. 维护一个单调递减队列
# 2. 每轮循环中，检查队首元素是否已经过时（被移出滑动窗口）
# 3. 弹出队首元素，为当前最大值
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        res = []
        for i in range(n):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            # while q and  i - q[0] + 1 <= k:
            while q and  i - q[0] >= k:   # 每轮循环中，检查队首元素是否已经过时（被移出滑动窗口）
                # res.append(nums[q[0]])   # 这里不需要添加到res里边
                # i-3, [i-2, i-1, i] # 例如k=3，则应该当q[0] <= i-k 的时候开始往外弹出 
                q.popleft()
            if i - k + 1 >= 0:   # 这是为了考虑前k-1个元素的情况
                res.append(nums[q[0]])
        return res