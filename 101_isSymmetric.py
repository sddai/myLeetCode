# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 【递归其实就是把各种条件写清楚，然后定义一个状态到另一个状态的转移公式】
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False 
            if left.val != right.val:
                return False
            if left.val == right.val:
                return helper(left.left, right.right) and helper(left.right, right.left)       
        if root == None:
            return True
        if root.left and root.right:
            return helper(root.left, root.right)
        elif root.left == None and root.right == None:
            return True
        else:
            return False


