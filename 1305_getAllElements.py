# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return None
            nonlocal temp_list
            dfs(root.left)
            temp_list.append(root.val)
            dfs(root.right)
        def merge(list1, list2):
            n1 = len(list1)
            n2 = len(list2)
            p1 = 0
            p2 = 0
            res = []
            while p1 < n1 and p2 < n2:
                if list1[p1] < list2[p2]:
                    res.append(list1[p1])
                    p1 += 1
                else:
                    res.append(list2[p2])
                    p2 += 1
            if p1 < n1:
                res.extend(list1[p1::])
            if p2 < n2:
                res.extend(list2[p2::])
            return res
        temp_list = []
        dfs(root1)
        list1 = temp_list
        temp_list = []
        dfs(root2)
        list2 = temp_list
        ans = merge(list1, list2)
        return ans
