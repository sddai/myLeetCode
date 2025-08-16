# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sum):
            if not root:
                return False
            if root.left == None and root.right == None and sum == root.val:
                return True
            left = dfs(root.left, sum - root.val) if root.left else False
            right = dfs(root.right, sum - root.val) if root.right else False
            return left or right 
        return dfs(root, targetSum)




'''        def dfs(root, sum):
            if not root:
                return 0
            nonlocal res
            sum + root.val
            dfs(root.left)
            dfs(root.right)
            if root.left is None and root.right is None:
                res.append(sum)
        sum = 0
        res = []
        dfs(root)'''