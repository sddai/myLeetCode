# 出错的原因在于没有添加dummy节点，导致错误处理需要删除链表第一个结点的情况
# 另外，由于n<=size，所以没有必要在第一个for loop里边判断fast为空
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val = 0, next = head)
        # p = head
        # slow = head
        # fast = slow
        # 【注意快慢指针法的初始化过程】
        # p = dummy
        slow = dummy
        fast = head
        # for i in range(n):
        # for i in range(n):
        #     if fast: 
        #         fast = fast.next
        #     else:
        #         return None
        for i in range(n):
            fast = fast.next
        # print(slow, fast)
        # if fast == None and slow == p:
        #     return 
        # if fast == None:
        #     return None
        # while slow and fast:
        while fast:
            # p = slow
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy.next  # 注意不要返回head
