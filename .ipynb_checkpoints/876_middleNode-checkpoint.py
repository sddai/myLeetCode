# 简单题
# 此题几乎一遍通过
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        slow = dummy
        fast = dummy.next
        while slow:
            slow = slow.next
            if fast == None or fast.next == None:
                return slow  # 注意这里前边已经有一次slow.next移动指针了，不用重复移动
            fast = fast.next.next
        return slow