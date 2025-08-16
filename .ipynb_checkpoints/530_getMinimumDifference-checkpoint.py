# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序遍历
        stack = []
        curr = root
        sorted_list = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:  # 这表明curr遍历到了最左下角的节点，左根右的“左”部分结束，现在需要从栈中弹出一个“根“，然后马上跟着一个“右”
                curr = stack.pop()
                sorted_list.append(curr.val)
                # stack.append(curr.right) #这句错了，不应该押入栈中，栈是用来保存根节点的，curr.right直接更新curr
                curr = curr.right
        ans = float("INF")
        for i in range(len(sorted_list) - 1):
            diff = sorted_list[i+1] - sorted_list[i]
            ans = min(ans, diff)
        return ans

'''# 这种解法兼顾了空间复杂度
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            if root == None:
                return 
            nonlocal prev
            nonlocal min_val
            inorder(root.left)
            if prev is not None: min_val = min(min_val, root.val - prev)
            prev = root.val
            inorder(root.right)
            return min_val
        prev = None
        min_val = float("INF")
        return inorder(root)'''


'''解法一不是很高效，空间复杂度高
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def inorder(root):
            if root == None:
                return
            nonlocal sorted_list
            inorder(root.left)
            sorted_list.append(root.val)
            inorder(root.right)
        sorted_list = []
        inorder(root)
        temp = float("INF")
        print(sorted_list)
        for i in range(len(sorted_list)-1):
            curr = sorted_list[i+1] - sorted_list[i]
            temp = min(temp, curr)
        return temp
'''
