# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 注意特殊情况的处理
        if root is None:
            return None
        p = root
        # while p: # 有递归就不用while循环了
        if p.val > key:
            # self.deleteNode(p.left, key)   # 这里写错了，要把返回值赋给p.left
            p.left = self.deleteNode(p.left, key)
        elif p.val < key:
            p.right = self.deleteNode(p.right, key)   # 同理
        else:    # 此时要删除的节点就是p
            # if p.left == None and p.right == None:  # p是叶子节点
            #     p = None
            if p.left == None or p.right == None:
                p = p.left if p.left else p.right
            # elif p.right:    # 要删除的p节点左子树为空
            #     p = p.right
            # elif p.left:
            #     p = p.left
            else:
                q = p.right
                while q.left:
                    q = q.left
                
                # q.right = p.right
                q.right = self.deleteNode(p.right, q.val)   # 在p（从root来的）的右子树中，把找到的这个最小的点删掉
                q.left = p.left  # 注意顺序：先删右子树，再删左子树，否则成环
                # p = q
                return q
        return p #注意返回的位置
                    
# 第二次通过：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root = self.delete(root, key)
        return root
    def delete(self, root, key):
        if not root:
            return None
        if root.val > key:
            # self.delete(root.left, key)
            root.left = self.delete(root.left, key)
        elif root.val < key:
            root.right = self.delete(root.right, key)
        elif root.val == key:
            # root = self.deleteNode(root, key)
            if not root.right:
                return root.left 
            elif not root.left:
                return root.right
            else:
                min_node = root.right
                while min_node.left:
                    min_node = min_node.left
                root.val = min_node.val
                root.right = self.delete(root.right, min_node.val) # root的左子树不变，右子树的最小值替换掉root.val（把右子树最小值转上来），再在右子树中删掉这个最小值
                # min_node.left = root.left
                # min_node.right = root.right 
                '''
                另一种写法更好：（不交换值，而是交换指针）
                # 处理情况 3
                # 获得右子树最小的节点
                minNode = getMin(root.right)
                # 删除右子树最小的节点
                root.right = deleteNode(root.right, minNode.val)
                # 用右子树最小的节点替换 root 节点
                minNode.left = root.left
                minNode.right = root.right
                root = minNode
                '''
        return root
            
    # # def deleteNode(self, root, key):
    #     # 这段代码只更新了形参root，没有改变实际的参数root
    #     # 此外，应该在衔接了min_node之后将原始的root删掉
    #     # print(root)
    #     if not root:
    #         return 
    #     p = root
    #     if not root.right:
    #         root = root.left
    #         return 
    #     if not root.left:
    #         root = root.right
    #         return 
    #     # 用右子树最小的节点【替换】 root 节点，因为这个数值比待删除点的所有子树都大，比所有右子树都小
    #     min_node = root.right
    #     while min_node.left:
    #         min_node = min_node.left
    #     min_node.left = root.left
    #     min_node.right = root.right 
    #     root = min_node
        
        