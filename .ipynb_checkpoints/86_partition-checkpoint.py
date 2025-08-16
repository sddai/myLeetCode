# 此题一遍通过
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_head1 = ListNode()
        p1 = dummy_head1
        dummy_head2 = ListNode()
        p2 = dummy_head2
        p = head
        while p:
            if p.val < x:
                p1.next = p   # 注意：ListNode类没有copy()方法
                p1 = p1.next
                p = p.next
                p1.next = None   # 注意把新建的链从原来的链接关系中断开，否则会成环
            else:
                p2.next = p
                p2 = p2.next
                p = p.next
                p2.next = None
        p1.next = dummy_head2.next
        return dummy_head1.next
'''
    # 另一种断开链的方法：
        # 不能直接让 p 指针前进，
        # p = p.next
        # 断开原链表中的每个节点的 next 指针
        temp = p.next
        p.next = None
        p = temp
'''