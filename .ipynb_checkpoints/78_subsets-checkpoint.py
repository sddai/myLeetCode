# 注意深浅拷贝问题
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, start):
            # nonlocal res # 不使用nonlocal也能通过
            # nonlocal path
            print(nums, res, path, start)

            # res.append(path) 
            # 【注意】如果这里每次都append path，则res里边是path的地址（引用），所以最后一轮结束后，res中的每一个path都指向最后一次更新过的path，res的每个元素都一样
            # 【解决方案】应该在每一次循环中把path里边的值取出来
            res.append(path[:])
            # if start == len(nums):
            #     return 
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(nums, i + 1)
                path.pop()
        res = []
        path = []
        dfs(nums, 0)
        return res

'''
class Solution:
    
    def __init__(self):
        self.res = []
        # 记录回溯算法的递归路径
        self.track = []

    # 主函数
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    # 回溯算法核心函数，遍历子集问题的回溯树
    def backtrack(self, nums: List[int], start: int) -> None:
        print(nums, self.res, self.track, start)
        # 前序位置，每个节点的值都是一个子集
        self.res.append(list(self.track))
        
        # 回溯算法标准框架
        for i in range(start, len(nums)):
            # 做选择
            self.track.append(nums[i])
            # 通过 start 参数控制树枝的遍历，避免产生重复的子集
            self.backtrack(nums, i + 1)
            # 撤销选择
            self.track.pop()
'''