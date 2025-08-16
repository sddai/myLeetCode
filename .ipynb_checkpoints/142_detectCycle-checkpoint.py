# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # 【注意】本题使用dummy_head可能会超时，应该令fast和slow在同一个点出发，比如都从dummy出发
        dummy.next = head
        # dummy = head
        fast = dummy
        slow = dummy
        # while fast.next  and fast:  # 注意fast和next的判断顺序
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        # print(fast, slow)
        # if fast != slow:
        if not fast or not fast.next:
            return None
        slow = dummy
        while fast != slow:
            fast = fast.next # 【易错】第二轮fast与slow都按照单位1的速度前进
            slow = slow.next
        return fast

        