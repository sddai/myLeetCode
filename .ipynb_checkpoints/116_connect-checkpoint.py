# 此题一遍通过
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root, ])
        while q:
            curr_layer = []
            last_node = None
            for curr in q:
                if curr:
                    if last_node:
                        last_node.next = curr
                    curr_layer.append(curr.left)        
                    curr_layer.append(curr.right)
                    last_node = curr
            if last_node: last_node.next = None
            q = curr_layer
        return root
        
        