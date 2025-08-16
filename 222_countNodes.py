# 简单题，一次通过
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def count(root):
            if not root:
                return 0
            else:
                return 1 + count(root.left) + count(root.right)
        return count(root)