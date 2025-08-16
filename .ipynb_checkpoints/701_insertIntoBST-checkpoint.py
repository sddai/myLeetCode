# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        p = self.insert_(root, val)
        return p
    def insert_(self, root, val):
        if not root:
            new_node = TreeNode(val = val)
            return new_node
        if root.val > val:
            root.left = self.insert_(root.left, val)
        elif root.val < val:  # 
            root.right = self.insert_(root.right, val)  # 笔误，错写成`self.right`
        return root