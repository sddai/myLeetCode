# 思路：找到中点，后半段反转，然后比对
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # dummy = ListNode(next=head) 
        # slow = dummy
        # fast = dummy
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        # 接下来reverse(slow)
        pre = None
        curr = slow
        next_ = slow 
        while curr:
            next_ = curr.next
            curr.next = pre
            pre = curr
            curr = next_
        p1 = head
        p2 = pre
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True
    
# 有dummy也一样：
# 思路：找到中点，后半段反转，然后比对
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(next=head) 
        slow = dummy
        fast = dummy
        # slow = head
        # fast = head
        # while fast and fast.next:
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        # 接下来reverse(slow)
        pre = None
        curr = slow
        next_ = slow 
        while curr:
            next_ = curr.next
            curr.next = pre
            pre = curr
            curr = next_
        # p1 = head
        p1 = dummy.next
        p2 = pre
        while p1 and p2:
            if p1.val == p2.val:
                p1 = p1.next
                p2 = p2.next
            else:
                return False
        return True