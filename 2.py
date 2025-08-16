# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_result = ListNode(0)
        l3 = l_result
        # p_curr = ListNode(0)
        # q_curr = ListNode()
        # p_curr.next = l1
        # q_curr.next = l2
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        while l1 or l2:
            sum = 0
            # carry = 0        
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2: 
                sum += l2.val
                l2 = l2.next

            sum += carry
            carry = sum // 10
            sum = sum % 10
            # l_result.val = sum
            l_result.next = ListNode(sum)
            l_result = l_result.next
            # return l_result
        if carry !=0:
            l_result.next = ListNode(carry)
        return l3.next


            
            # if p_curr.next 
            # sum = p_curr.val + q_curr.val + carry
            # carry = int(sum / 10)
            # sum = sum % 10
            # l_result.val = sum
            # l_result.next = carry

        
        # return 


