# 解题注意事项：要添加头指针，最后返回的是头指针的next，而不要把最后一个指向最终节点的引用返回去

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def traverse(head):
            if not head:
                return 0
            nonlocal num
            traverse(head.next) 
            num = num * 10 + head.val
        def build_linked_list(num):
            head = ListNode()
            p = head
            while num != 0:
                p.val = num % 10
                num = num // 10 
                if num != 0:
                    p.next = ListNode()
                    p = p.next
            p = None
            return head
        num = 0
        traverse(l1)
        num1 = num
        num = 0
        traverse(l2)
        num2 = num
        res = num1 + num2
        print(res)
        return build_linked_list(res)



'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        f=0
        if l1 is None: #python原来用is判断啊
            return l2
        if l2 is None:
            return l1
        l3=ListNode(0) #每个节点都要new一个
        res =l3
        while l1 or l2:   #python 原来是or啊
            summ=0
            if l1 :
                summ+=l1.val
                l1=l1.next
            if l2 :
                summ+=l2.val
                l2=l2.next
            if (summ+f)>9 :
                res.next=ListNode(summ+f-10)
                f=1
            else :
                res.next=ListNode(summ+f)
                f=0
            res=res.next
        if f!=0:
            res.next=ListNode(f)
        return l3.next
'''
