# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 此题需要找好递归形参之间的递进关系

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preorder, inorder, preStart, preEnd, inStart, inEnd):
            if preStart > preEnd:
                return None
            root_val = preorder[preStart]
            root = TreeNode(root_val)
            root_inorder_index = get_inorder_index[root_val]
            # len_left = root_inorder_index # 这里要减去inStart
            len_left = root_inorder_index - inStart
            left_preStart = preStart + 1
            left_preEnd = left_preStart + len_left - 1  
            # left_preEnd = left_preStart + len_left
            left_inStart = inStart
            left_inEnd = root_inorder_index - 1
            root.left = build(preorder, inorder, left_preStart, left_preEnd, left_inStart, left_inEnd)
            right_preStart = preStart + len_left + 1
            right_preEnd = preEnd
            right_inStart = root_inorder_index + 1
            right_inEnd = inEnd
            root.right = build(preorder, inorder, right_preStart, right_preEnd, right_inStart, right_inEnd)
            return root

        get_inorder_index = dict()
        for i, node in enumerate(inorder):
            get_inorder_index[node] = i
        n = len(preorder)
        root = build(preorder, inorder, 0, n-1, 0, n-1)
        return root