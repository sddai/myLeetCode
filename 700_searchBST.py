# 本题一次通过
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.dfs(root, val)
    def dfs(self, root, val):
        if not root:
            return None
        if root.val < val:
            return self.dfs(root.right, val)
        elif root.val > val:
            return self.dfs(root.left, val)
        else:
            return root