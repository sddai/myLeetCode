# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 本题一次通过
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def find_depth(root):
            if not root:
                return 0
            if root.left:
                left = find_depth(root.left) + 1
            else:
                left = 0
            if root.right:
                right = find_depth(root.right) + 1
            else:
                right = 0
            nonlocal max_depth
            max_depth = max(max_depth, left + right)
            return max(left, right)
        max_depth = 0
        find_depth(root)
        return max_depth

# 第二次通过
# 本题其实就是计算顶点数（或者深度）的递归做法加上一个额外计算左右两支深度之和（直径）的过程
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(root ):
            nonlocal diameter
            if not root:
                return 0
            l = helper(root.left ) + 1
            r = helper(root.right ) + 1
            max_depth = max(l, r)
            diameter = max(diameter, l + r - 2)    # l + r是顶点数，要减2变成边数
            return max_depth
        diameter = 0
        helper(root )
        return diameter
             