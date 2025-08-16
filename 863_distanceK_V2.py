# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        def build_graph():
            queue = [root]
            while queue:
                p = queue.pop(0)
                if p.left:
                    graph[p.val].append(p.left.val)
                    graph[p.left.val].append(p.val)
                    queue.append(p.left)
                if p.right:
                    graph[p.val].append(p.right.val)
                    graph[p.right.val].append(p.val)
                    queue.append(p.right)
        build_graph()
        # print(graph)
        visited = set([target.val])
        queue = [target.val]
        distance = 0
        '''
        while queue and  k:   # !!!发现的现象：这里用k递减能过，用distance递加则不过
                              # !!!这个现象的解释：如果用distance，应该递加到k-1，而不是k
            curr_layer = []
            # curr_layer = [target.val]
            for q in queue:
                for neighbor in graph[q]:
                    if neighbor not in visited:
                        curr_layer.append(neighbor)
                        visited.add(neighbor)
                        # queue.append(neighbor)
                         # d += 1
            queue = curr_layer
            # 在遍历了当前层的所有邻居之后，改变queue的值
            k -= 1
            print("k=:")
            print(k)
            '''
        
        while queue and distance <= k-1:
            curr_layer = []
            # curr_layer = [target.val]
            for q in queue:
                for neighbor in graph[q]:
                    if neighbor not in visited:
                        curr_layer.append(neighbor) # curr_layer的作用仅在于记录当前层的节点是哪些，真正循环的还是queue
                        visited.add(neighbor)
                        # queue.append(neighbor)
                         # d += 1
            queue = curr_layer
            # 在遍历了当前层的所有邻居之后，改变queue的值
            distance += 1
            print("distance=:")
            print(distance)
            # if distance == k: result = curr_layer
        
        return queue
