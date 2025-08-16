# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 此题的关键是不用纠结父节点通路能涂到的颜色数量，因为左右子树的节点数好计算，总数n减去左右子树即得到父节点通路的节点数（面积）

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def find_area(root):
            if not root:
                return 0
            left = find_area(root.left)   
            # left = find_area(root.left) + 1
            # 此题易错点：不要在这里的左右分别加一，因为每次迭代只有一个root，面积只加一次，也就是在return里边加一
            right = find_area(root.right)
            nonlocal area_left 
            nonlocal area_right
            if root.val == x:
                area_left = left 
                area_right = right 
            return left + right + 1
        area_left = 0
        area_right = 0
        find_area(root)
        areas = [area_left, area_right, n - area_left - area_right - 1]
        print(areas)
        for area in areas:
            if area > n // 2:
                return True
        return False

