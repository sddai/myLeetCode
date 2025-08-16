# 这是一个二叉树版的前缀和（从大到小倒序的前缀和，后序遍历）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum_ = 0
        self.dfs(root)
        return root
    def dfs(self, root):
        if not root:
            return 
        self.dfs(root.right)
        self.sum_ += root.val
        root.val = self.sum_
        self.dfs(root.left)
        # if not root:
        #     return 0
        # right = self.dfs(root.right)
        # val = root.val
        # left = self.dfs(root.left)
        # if root.left: 
        #     root.left = val + right 
        # return val