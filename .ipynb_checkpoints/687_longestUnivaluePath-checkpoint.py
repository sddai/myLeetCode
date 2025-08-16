# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 【此题与124的区别】：124中，存在两种情况，即只选择左或者右中的一个分支，或者选两个分支
# 本题中，根节点处的长度等于左右分支长度之和
# 【最长同值路径长度必定为某一节点的左最长同值有向路径长度与右最长同值有向路径长度之和。】
# ！！！此题的一个关键点在于：
# 每次递归中，沿着递归函数向上返回的值是左右子树中较大的那一个分支，但是总体记录下来的ans（或者说结果）却是这两个分支的和（注意不是递归的返回值），要区分二者。

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def find_max(root):
            if not root:
                return 0
            nonlocal count
            l = find_max(root.left)
            r = find_max(root.right)
            if root.left and root.val ==  root.left.val:
                case1 = l + 1
            else:
                case1 = 0
            if root.right and root.val == root.right.val:
                case2 = r + 1
            else:
                case2 = 0
            count = max(count, case1 + case2)  # 当前路径长度等于左子树长度与右子树长度之和
            return max(case1, case2)  # 这里把左右分支中的较大的一个分支作为返回值，返回给递归函数
        count = 0
        find_max(root)
        return count

'''
TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
    case2 = max(r+1, 0)

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def find_max(root):
            if not root:
                return 0
            nonlocal count
            curr = root.val
            l = find_max(root.left)
            r = find_max(root.right)
            if root.left and root.right:
                if root.val == root.left.val and root.val == root.right.val:
                    case1 = l + r + 2
                    count = max(count, case1)
                # 在这里加上一句else: case1 = 0 # 就可以避免返回值流程复杂的问题
                if root.val ==  root.left.val:
                    case2 = max(l+1, 0)
                    count = max(count, case2)
                    return case2
                if root.val == root.right.val:
                    case2 = max(r+1, 0)
                    count = max(count, case2)
                    return case2
                return 0
            if root.left:
                if root.val ==  root.left.val:
                    case2 = max(l+1, 0)
                    count = max(count, case2)
                    return case2
                else:
                    return 0
            if root.right:
                if root.val == root.right.val:
                    case2 = max(r+1, 0)
                    count = max(count, case2)
                    return case2
                else:
                    return 0
        count = 0
        return find_max(root)'''