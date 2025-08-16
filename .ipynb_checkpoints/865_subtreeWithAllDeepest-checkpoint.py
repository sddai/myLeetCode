# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
本题的【解题思路】：
利用递归的思想。
首先，要明确只有当左子树和右子树的深度相同时，我们才返回以当前结点为根的子树！否则递归深度更深的左右子树。
'''

from collections import defaultdict
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        deepest = set([])
        queue = [root]
        depth = 0
        depth_dict = defaultdict(int)
        while queue:
            curr_layer = []
            depth += 1
            for curr in queue:   # 树形结构不用记录已访问节点visited
                # p = queue.pop(0)  # 已经用了for循环就不要用pop(0)
                depth_dict[curr.val] = depth
                if curr.left:
                    curr_layer.append(curr.left)
                if curr.right:
                    curr_layer.append(curr.right)
            queue = curr_layer
        max_depth = max(depth_dict.values())

    def ans(node: TreeNode) -> TreeNode:
        if not node or depth_dict[node.val] == max_depth:
            return node
        left = ans(node.left)
        right = ans(node.right)
        # 这个递归过程的思路是：如果最深的节点分布在当前node的左右两个分支里边，则返回当前节点node，否则返回含有最深节点的那个分支
        if left and right:
            return node
        else:
            if left: return left
            if right: return right
    return ans(root)

    # 这里的ans函数不好理解，另一种写法：
    # 下边的deep就是求深度depth
    def deep(self, tree): #计算树的深度，上边是从上向下求深度，root的深度是0，此解法是从下往上求深度，叶子节点深度是0
        if tree == None:
            return 0
        return max(self.deep(tree.left), self.deep(tree.right)) + 1

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if root.left == None and root.right == None:   #这两行代码不要也行，因为deep函数参数可以为None
            return root
        left_deep = self.deep(root.left)
        right_deep = self.deep(root.right)
        if left_deep == right_deep:
            return root
        else:
            return self.subtreeWithAllDeepest(root.left) if left_deep > right_deep else self.subtreeWithAllDeepest(root.right)

'''
一种错误写法：
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        deepest = set([])
        queue = [root]
        depth = 0
        depth_dict = defaultdict(int)

        while queue:
            curr_layer = []
            depth += 1
            for curr in queue:   # 树形结构不用记录已访问节点visited
                depth_dict[curr.val] = depth
                if curr.left:
                    curr_layer.append(curr.left)
                if curr.right:
                    curr_layer.append(curr.right)
            queue = curr_layer
            deepest = set([i for i in curr_layer])
            # 最后一轮退出内层for循环的时候，curr_layer里边是叶子结点的子节点（也就是None）
            # 所以当退出全部的两层循环中之后，curr_layer里边并没有保存最深的叶子结点，而是保存了叶子结点下边的None -> 正是这个None的存在，才使得两层循环退出的
            # 解决办法是：用if判断当前节点为叶子结点，并提前退出
'''