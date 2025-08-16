# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param root TreeNode类 
# @param target double浮点型 
# @param m int整型 
# @return int整型一维数组
#
import heapq
class Solution:
    def findClosestElements(self , root: TreeNode, target: float, m: int) -> List[int]:
        # write code here
        hq = []
        # q_size = 0
        def traverse(root, hq):
            if not root:
                return
            curr = root.val
            heapq.heappush(hq, (abs(target - curr), curr))
            traverse(root.left, hq)
            traverse(root.right, hq)
        traverse(root, hq)
        res = []
        for i in range(m):
            v = heapq.heappop(hq)
            res.append(v[1])
        res.sort()
        return res





