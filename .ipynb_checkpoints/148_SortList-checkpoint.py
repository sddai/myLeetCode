# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
        # 三部曲：split->sort->merge，但是只需要写两个函数：sort， merge
        # sort 递归调用自身，merge用于合并

        # def split(head):
        #     fast = head
        #     slow = head
        #     while fast.next:
        #         fast = fast.next.next
        #         slow = slow.next
        #     mid = slow
        #     p1 = head
        #     p2 = mid.next
        #     return p1, p2
        
        def sort(head):
            if head is None or head.next is None:   # 这是退出递归的条件
                return head
            fast = head.next
            slow = head
            while fast and fast.next:   # 注意判断条件：何时走到链表结尾
                fast = fast.next.next
                slow = slow.next
            mid = slow.next
            slow.next = None   # 每次归并中，划分成两个序列之后要从中间断开！！！
            # p1, p2 = split(head)
            return merge(sort(head), sort(mid))

        def merge(p1, p2):
            # if p1 == p2:       # 递归的停止条件，要写在递归里边，不能写在合并里边
            #     return p1
            # else:
            t1 = p1
            t2 = p2
            head = ListNode(val=0, next=None)   # 这里要用两个指针，其中一个要保留在头指针处
            t = head
            while t1 and t2:
                if t1.val < t2.val:
                    t.next = t1
                    t1 = t1.next
                    t = t.next
                else:
                    t.next = t2
                    t2 = t2.next
                    t = t.next
            if t1:
                t.next = t1
            elif t2:
                t.next = t2
            return head.next   # 这里返回的是head，不要返回t
        return sort(head)

                