# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.successor = None
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # if left == 0:
        if left == 1:
            return self.reverse(head, right)
        # # head.next
        # return self.reverseBetween(head.next, left - 1, right - 1)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
    def reverse(self, head, right):
        if right == 1:
            # head.next = self.successor  # 写反了，需要记录下来反转处的边界
            self.successor = head.next
            return head
        # head.next.next = head   # 注意这里需要先记录下来last指针然后再连接head.next.next
        last = self.reverse(head.next, right - 1)
        head.next.next = head
        head.next = self.successor
        return last