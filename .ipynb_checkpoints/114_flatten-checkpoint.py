# 第二次通过
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flat(root)

    def flat(self, root):
        if not root:
            return root
        left = self.flat(root.left)
        right = self.flat(root.right)
        root.left = None
        root.right = left
        p = root
        while p.right:   # 把整理之后的右子树最后一个节点接上来
            p = p.right
        p.right = right

        # if left:
        #     root.right = left
        #     root.left = None
        #     left.right = right    # 这样只链接了第一个节点，后边的节点没有连接到链上
        # else:
        #     root.right = right
        # tmp = self.flat(root.left)
        # root.left = None
        # if tmp: 
        #     tmp.right = self.flat(root.right)
        # # else:
        #     # tmp = 
        # root.right = tmp
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
       
        """
        # queue = [root]
        # next = None
        ''' 注意此题的易错点：此题返回值是None，必须以inplace的方式在原始二叉树上边进行修改，所以使用new_root进行复制的方法不正确
        def dfs(root, new_root):       #【思考】为什么不能正向进行前序遍历？
            if not root:
                return None
            # nonlocal new_root
            new_root.left = None
            new_root.right = TreeNode(root.val)
            new_root = new_root.right  # 如果这么写，迭代结束之后new_root指向遍历序列的末尾，不应该返回这个不断向下的指针
            dfs(root.left, new_root)
            dfs(root.right, new_root)
        head = TreeNode(0)
        p = head
        # dfs(root, p)#
        return head'''
# 正确解法：
        prev = None
        def dfs(root):   # 反序遍历，【思考】为什么不能正向进行前序遍历？
            if not root:
                return None
            dfs(root.right)
            dfs(root.left)
            root.left = None
            nonlocal prev
            root.right = prev
            prev = root
        dfs(root)


'''     def dfs(root, new_root):       #【思考】为什么不能正向进行前序遍历？
            # 例：1 2 3 4 5 6，原因就是我们把 1 的右指针指向 2，那么 1 的原本的右孩子就丢失了，也就是 5 就找不到了。解决方法的话，我们可以逆过来进行。我们依次遍历 6 5 4 3 2 1，然后每遍历一个节点就将当前节点的右指针更新为上一个节点。
            if not root:
                return None
            # nonlocal new_root
            new_root.left = None
            new_root.right = TreeNode(root.val)
            new_root = new_root.right
            dfs(root.left, new_root)
            dfs(root.right, new_root)
        new_root = TreeNode(0)
        dfs(root, new_root)
        return new_root.right'''
'''如下是bfs的方法，本题应该用dfs
        while queue:
            currNode = queue.pop(0)
            if currNode:
                queue.append(currNode.left)
                queue.append(currNode.right)
                # currNode.left = None
                # if next:
                #     next = currNode
                # next = currNode.right
                new_root.left = None
                new_root.right = TreeNode(currNode.val)
        return new_root'''