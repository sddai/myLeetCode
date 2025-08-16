# 此题一遍通过
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            if not root:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            return max(l, r) + 1
        return helper(root)