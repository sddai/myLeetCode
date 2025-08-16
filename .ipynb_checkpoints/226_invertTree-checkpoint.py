# 此题一遍通过
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)
    def invert(self, root):
        if not root:
            return root
        l = self.invert(root.right)
        r = self.invert(root.left)
        root.left, root.right = l, r
        return root