# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 下边这么写也过了
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def helper(root, max_val, min_val):
#             if not root:
#                 return True
#             return root.val < max_val and root.val > min_val
#             helper(root.left, root.val, min_val)
#             helper(root.right, max_val, root.val)
#         max_val = float("inf") 
#         min_val = -float("inf")
#         return helper(root, max_val, min_val)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, max_val, min_val):
            if not root:
                return True
            if root.val < max_val and root.val > min_val:
                return helper(root.left, root.val, min_val) and helper(root.right, max_val, root.val)
            else:
                return False
        max_val = float("inf") 
        min_val = -float("inf")
        return helper(root, max_val, min_val)

'''
递归法：
【核心就是在向左右子树递归过程中不断更新上下界】:
如果该二叉树的左子树不为空，则左子树上所有节点的值均小于它的根节点的值； 若它的右子树不空，则右子树上所有节点的值均大于它的根节点的值
1. 每次判断当前节点是否在上下界之内，不在界内返回false
2. 递归左子树：当前节点node.val作为上界，递归左子树node.left
3. 递归右子树：当前节点node.val作为下界，递归右子树node.right
4. 要注意初始条件：第一层循环，没有前驱节点，所以上下界设置为inf
【方法二】：更好
中序遍历，判断中序遍历结果是否递增
'''
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         def helper(root, min_val, max_val) -> bool:
#             if root:
#                 if root.val > min_val and root.val < max_val:
#                     return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)
#                 else:
#                     return False
#             return True
#         return helper(root, float('-INF'), float('INF'))
