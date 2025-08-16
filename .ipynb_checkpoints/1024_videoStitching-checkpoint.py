# 第二次提交
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        clips.sort(key = lambda x: x[0])
        if clips[0][0] != 0:
            return -1
        # start = 0
        # end = clips[0][1]  #【易错】需要注意end从0开始
        end = 0
        t = 0
        cnt = 0
        i = 0
        # for i in range(1, n):   # 像此题用for循环不好确定i之间的关系，可以考虑使用while循环
        while i < n:
            # if clips[i][0] <= end:   # 反复判断，用while替换if
            while  i < n  and clips[i][0] <= end:
                t = max(t, clips[i][1])
                i += 1
            end = t
            cnt += 1
            if end >= time:   # 注意最后边这两个if的顺序
                return cnt
            if  i < n  and clips[i][0] > end:
                return -1
        
        return -1        

# 【贪心策略】：排序之后，从第一个区间开始选，每当选中一个区间 x，我们会比较所有起点小于 x.start 的区间，根据贪心策略，它们中终点最大的那个区间就是下一个会被选中的区间，以此类推。
# 注意看函数签名，time和clips都是整数int
# 动态规划：令 dp[i] 表示将区间 [0,i) 覆盖所需的最少子区间的数量。【动态规划其实就是初始情况+枚举各种情况】
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [float("inf") for _ in range(time+1)]
        dp[0] = 0
        for i in range(1, time+1):
            for start_i, end_i in clips:
                if i <= end_i and i > start_i:
                    dp[i] = min(
                        dp[i], 
                        dp[start_i] + 1
                    )
        return dp[-1] if dp[-1] < float("inf") else -1

'''     clips.sort(key = lambda x: x[0])
        if clips[0][0] != 0:
            return -1
        n = len(clips)
        left = 0
        right = 0
        num_clips = 0
        for i, (start, end) in enumerate(clips):
            if start <= left:
                right = max(right, end)
            else:
                num_clips += 1
                left = right
            if right == time:
                return num_clips
        return -1
'''