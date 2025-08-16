from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def create(operations: [[int]]) -> Node:
    root = Node(-1)
    # root.val = -1
    index_to_node = dict()
    index_to_node[0] = root
    count = 0
    for height, index in operations:
        id_ = 2 ** height - 1 + index
        if id_ not in index_to_node:
            # if count == 6: print(id_, index_to_node)
            index_to_node[id_] = Node(None)
            index_to_node[id_].left = Node(count)
            index_to_node[id_*2 + 1] = index_to_node[id_].left
            # count += 1
        if not index_to_node[id_].left:
            index_to_node[id_].left = Node(count)
            index_to_node[id_*2 + 1] = index_to_node[id_].left
            # count += 1
        elif not index_to_node[id_].right:
            index_to_node[id_].right = Node(count)
            index_to_node[id_*2 + 2] = index_to_node[id_].right
            # count += 1
        count += 1
        # else:
        # index_to_node[id_] = node
    node_index = [key for key in index_to_node.keys()]
    node_index.sort()
    ans = []
    for i in range(node_index[-1] + 1):   # 输出不应该按照list存储二叉树的方法输出，而应该只输出子节点
        if i in index_to_node:
            ans.append(index_to_node[i].val)
        else:
            ans.append(None)
    print(ans)
    return root

# def print_tree(ans, root):
#     # p = root
#     q = deque([root])
#     # q = [root]
#     while q:
#         curr = q.popleft()
#         ans.append(curr.val)
#         q.append(curr.left)
#         q.append(curr.right)
    
operations = [[0, 0], [0, 0], [1, 1], [1, 0], [0, 0]]
create(operations)
operations = [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 1], [2, 0], [3, 1], [2, 0]]
create(operations)