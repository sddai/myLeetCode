# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 本题的关键是：通过返回值将上一轮递归结果和本轮递归结果联系起来，即，向下递归找到要删除的节点，通过return返回一个None给他的父节点。这种结构替代了原思路中使用prev记录上轮迭代节点地址的方法
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def dfs(root):  #这个递归函数，接受一个根节点，返回已经处理过的根节点
            if not root:
                return None
            nonlocal ans
            root.left = dfs(root.left) # 1. if root.right else None # 由于一进入dfs就进行了判断，所以这里不用重复判断
            root.right = dfs(root.right) # 2. 这里要写一个递归，递归更新root.left。而不要用l或者r这种新变量名，也就是说，要在原始的那棵树上更新，否则最终的root没变，要删除的节点没删除干净 3. 可以类比这里其实是一个自底向上的过程
            if root.val in delete_set:
                if root.left: ans.append(root.left)
                if root.right: ans.append(root.right)
                return None
            return root # 注意最后要返回root本身
        delete_set = set(to_delete)
        ans = []
        root = dfs(root)
        if root :
            ans.append(root)
        return ans

pri
'''
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def delete_func(root):
            if not root:
                return None
            nonlocal ans
            nonlocal delete_set
            prev = None
            if prev and  root.val in delete_set:   # 不要用这种prev的办法去将删除节点置为None -> 直接在一遍遍历中将要删除的root.left或者root.right置为None
                prev_node = prev[0]
                if prev[1] == "left":
                    prev_node.left = None
                if prev[1] == "right":
                    prev_node.right = None
            if root.val in delete_set:
                if root.left:  
                    delete_func(root.left)   # 注意这两句的顺序
                    ans.append(root.left)     # 注意这两句的顺序
                    prev = (root, "left")
                    print("######")
                if root.right:
                    delete_func(root.right)
                    ans.append(root.right)
                    prev = (root, "right")
                    print("######")
                prev = root
        
        delete_set = set(to_delete)   # delete_set: set[int]
        ans = []
        delete_func(root)
        return ans
'''
