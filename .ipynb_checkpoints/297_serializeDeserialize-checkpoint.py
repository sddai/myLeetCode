# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root: 
            serial = str(root.val) + "," + self.serialize(root.left) + "," + self.serialize(root.right)
            return serial
        else:
            return str("null")
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # 下边这个是BFS的写法，本题使用DFS的写法
        # serial = data.split(",")
        # if serial[0] == "null": return []
        # if serial[0] != "null": root = TreeNode(int(serial[0]))
        # queue = [root]
        # i = 1
        # # for i in range(1, len(serial), 2):
        # while queue:
        #     node = queue.pop(0)
        #     if serial[i] != "null":
        #         node.left = TreeNode(int(serial[i]))
        #         queue.append(node.left)
        #     i = i + 1
        #     if serial[i+1] != "null":
        #         node.right = TreeNode(int(serial[i+1]))
        #         queue.append(node.right)
        #     i = i + 1 
        def dfs(serial):
            val = serial.pop(0)
            if val == "null":
                return None
            else:
                new_node = TreeNode(int(val))
                new_node.left = dfs(serial)
                new_node.right = dfs(serial)
                return new_node
        serial = data.split(",")
        root = dfs(serial)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


# 第二次通过
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                return "#"
            l = helper(root.left)
            r = helper(root.right)
            return str(root.val) + "," + l + "," + r
        # s = []
        # print(helper(root))
        return helper(root)
            
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(s):
            # print(s)
            if s[0] == "#":
                s.popleft()   # 或者一进入函数就进行popleft
                return None
            root = TreeNode(val = s[0])
            s.popleft()
            root.left = helper(s)
            root.right = helper(s)
            return root
        s = data.split(",")
        s = deque(s)
        # print(s)
        return helper(s)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))