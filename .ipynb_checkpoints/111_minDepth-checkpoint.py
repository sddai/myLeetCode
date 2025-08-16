# 此题注意示例2的特殊情况：当root的左子树为空的时候，depth为非空子树的高度
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            # if root.left == None and root.right == None:
                # return 0
            if root.left == None or root.right == None:
                return max(dfs(root.left) + 1, dfs(root.right) + 1)
            return min(dfs(root.left) + 1, dfs(root.right) + 1)
        return dfs(root)

    
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def searchDepth(root):
            # 如果不过，这里边注意将各种条件写清楚：
            # 1.左孩子和有孩子都为空的情况，说明到达了叶子节点，直接返回1即可
            # 2.如果左孩子和由孩子其中一个为空，那么需要返回比较大的那个孩子的深度
            #  （其中一个节点为空，说明m1和m2有一个必然为0，所以可以返回m1 + m2 + 1）
            # 3.最后一种情况，也就是左右孩子都不为空，返回最小深度+1即可
            if root == None:
                return 0
            if root.left and root.right:
                l = searchDepth(root.left)
                r = searchDepth(root.right)
                return min(l, r) + 1
            if root.left:
                return searchDepth(root.left) + 1
            if root.right:
                return searchDepth(root.right) + 1
            if root.left == None and root.right == None:
                return 1
        return searchDepth(root)
'''