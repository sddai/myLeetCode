# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)
    
    def reverse(self, head):
        if not head or not head.next:
            return head
        last = self.reverse(head.next)
        # last.next = head   # 注意，last一直递归下去，最后会返回尾部节点，所以下边应该使用head.next.next将两段链表链接起来
        head.next.next = head # 核心是两个head的反转，从后往前执行，逐个反转
        head.next = None
        return last