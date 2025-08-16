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
                return None
            # left = None
            # right = None
            if root.val == p or root.val == q:
                return root
            if root.val > q:
                # left = find(root.left, p, q)
                return find(root.left, p, q)
            elif root.val < p:
                # right = find(root.right, p, q)
                return find(root.right, p, q)
            else:
                return root
            # left = find(root.left, p, q)
            # right = find(root.right, p, q)
            # if left and right:
                # return root
            # return left if left else right 
        v1 = min(p.val, q.val)
        v2 = max(p.val, q.val)
        return find(root, v1, v2)