# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0, 0) # dfs[0]表示不取根节点，dfs[1]表示取根节点
            left = dfs(root.left)
            right = dfs(root.right)
            choose = root.val + left[0] + right[0]
            not_choose = max(left[0], left[1]) + max(right[0], right[1])
            return (not_choose, choose)
        res = dfs(root)
        return max(res)
        
            