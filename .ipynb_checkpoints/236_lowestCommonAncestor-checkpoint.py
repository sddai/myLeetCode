# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root, p, q):
            if not root:
                return False
            if root.val == p.val or root.val == q.val:
                return root   # 当p是q的父节点的时候，由其他分支返回来的都是False，只有这里返回了一个root，此时不需要再往下递归，q一定在下边
            left = find(root.left, p, q)
            right = find(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        return find(root, p, q)