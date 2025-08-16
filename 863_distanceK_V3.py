# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        p = root
        queue = [root]
        visited = set([])
        if k == 0:   # 用例不全的原因在于没处理特殊情况
            return [target.val]
        while queue:
            curr = queue.pop(0)
            if curr not in visited and curr.left: 
                graph[curr.val].append(curr.left.val)
                graph[curr.left.val].append(curr.val)
                queue.append(curr.left)
            if curr not in visited and curr.right: 
                graph[curr.val].append(curr.right.val)
                graph[curr.right.val].append(curr.val)
                queue.append(curr.right)
            visited.add(curr)
        print(graph)
        queue = [target.val]
        visited = set([target.val])
        distance = 0
        while queue:   
            # 整体的逻辑是：每一次进入while循环都是一层，在这一层用for遍历这一层中的每一个q，然后下一层刷新queue为新的一层
            curr_layer = []
            # curr = queue.pop(0)   遍历queue中每个节点
            for curr in queue:
                for neighbor in graph[curr]:
                    if neighbor not in visited:     # 注意判断已经访问的节点！！！
                        curr_layer.append(neighbor)
                        visited.add(neighbor)
            queue = curr_layer
            # print(ans)
            distance += 1
            if distance == k:
                break
            # for neighbor in graph[curr]:
            #     curr_layer.append(neighbor)
            #     visited.add(neighbor)
            #     if distance == k:
            #         quit = 1
            #     else:
            #         for neighbor in curr_layer:
            #             queue.append(neighbor)
            # distance += 1
        return queue
                
            
            