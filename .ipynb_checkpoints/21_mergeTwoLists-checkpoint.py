# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    p1 = list1
    p2 = list2
    head = ListNode(0, next=None)
    p = head
    while p1 and p2:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
            p = p.next
        else:
            p.next = p2
            p2 = p2.next
            p = p.next
    if p1:
        p.next = p1
    elif p2:
        p.next = p2

    return head.next