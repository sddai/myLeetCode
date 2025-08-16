# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        last = head
        for i in range(k):  # 左闭右开区间
            if last:
                last = last.next
            else:
                return head
        reversed = self.reverse(head, last)
        head.next = self.reverseKGroup(last, k)   # 左闭右开区间
        return reversed
    def reverse(self, head, last):
        pre = None
        curr = head
        next = curr
        # while curr != None:
        # for i in range(k):
        #     if curr == None:
        #         break
        #     next = curr.next
        #     curr.next = pre
        #     next.next = curr
        while curr != last:
            next = curr.next   # 注意一次循环只需要连接（反转）一个连接
            curr.next = pre
            pre = curr
            curr = next
        # curr.next = pre   # 这句在循环里边已经执行过了
        return pre  # 注意反转的是[a, b)左闭右开区间

'''
# 第二次通过
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        start = head
        end = head
        for i in range(k):
            if end == None:
                return head
            end = end.next
        reversed_ = self.reverse(start, end)
        # end.next = self.reverseKGroup(end, k)   # 这句链接有问题，start指向反转前的head，通过reverse函数之后start指向的点变成了结尾，为了链接起来，应该将start指向下一轮k个反转之后的头结点，也就是start.next = reverseKG(next_K)
        start.next = self.reverseKGroup(end, k)
        return reversed_

    def reverse(self, head, tail):
        # if head == None:
        #     return None  #   这段多余，head为空的时候，返回pre就行
        pre = None
        curr = head
        next_ = head
        while curr != tail:
            next_ = curr.next
            curr.next = pre
            pre = curr
            curr = next_
        return pre

'''