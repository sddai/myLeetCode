# Definition for a binary tree node.
# 此题不通过平台提交需要自定义输入的结构，因此在服务器上自己运行不通过
from collections import defaultdict
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def distanceK( root: TreeNode, target: TreeNode, k: int) -> [int]:
    graph = defaultdict(list)
    def build_tree(p):
        if not p:
            return
        if p.left: 
            graph[p.val].append(p.left.val)
            graph[p.left.val].append(p.val)
        if p.right:
            graph[p.val].append(p.right.val)
            graph[p.right.val].append(p.val)
        build_tree(p.left)
        build_tree(p.right)
        return
    build_tree(root)
    # while queue:       # 出错的地方还在于建立graph的方式忽略了节点为null这种情况，示例使用递归建图，通过
    #     p = queue.pop(0)

    queue = [target.val]
    visited = set([target.val])
    # print(graph)
    d = 0
    # selected = []
    # if k == 0:
    #     return selected.append(target.val)   # 这里错了：k的判断包含在while里边
    while queue and k:
        # curr = queue.pop(0) # 出错的关键在于遍历的方式：逐层遍历，逐层得到邻居curr_list
        curr_list = []
        for curr in queue:
            for neighbor in graph[curr]:
                if neighbor not in visited:
                    # queue.append(neighbor)
                    visited.add(neighbor) 
                    curr_list.append(neighbor)
        k -= 1
        queue = curr_list
    return queue

print(distanceK([0,1,None,None,2,None,3,None,4], 3, 0))
    
    
    
'''
一直没有过的一个测试用例是：
[0,1,None,None,2,None,3,None,4]
3
0
输出：
null
预期结果：
[3]

另一个例子是，结果需要返回[]，结果返回的是null
'''

        # while queue and d<=k:
        #     # curr = queue.pop(0) # 出错的关键在于遍历的方式：逐层遍历，逐层得到邻居curr_list
        #     curr_list = []
        #     for curr in queue:
        #         for neighbor in graph[curr]:
        #             if neighbor not in visited:
        #                 # queue.append(neighbor)
        #                 visited.add(neighbor) 
        #                 curr_list.append(neighbor)
        #     d += 1
        #     # print(curr_list)
        #     queue = curr_list
        #     if d == k:
        #         selected = queue
        # return selected