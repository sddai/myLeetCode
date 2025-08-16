# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def flip(root):
            if root:
                root.left, root.right = root.right, root.left
        if root1 == None and root2 == None:
            return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            # if root1.left == root2.left and root1.right == root2.right:
            return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) ) or \
                (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
            # flip(root2)
            # return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if root1 or root2:
            return False
'''错误写法：不应该显式调用flip对root2进行翻转，而应该通过函数调用位置进行翻转
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def flip(root):
            if root:
                root.left, root.right = root.right, root.left
        if root1 == None and root2 == None:
            return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            if root1.left == root2.left and root1.right == root2.right:
                return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            flip(root2)
            return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        if root1 or root2:
            return False'''
            
        
            