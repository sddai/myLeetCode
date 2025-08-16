# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
这段代码的功能是对一个链表进行排序，使用了归并排序的方法。具体的解释如下：

- 定义一个类Solution，有一个方法sortList，接受一个链表的头节点head作为参数，返回排序后的链表的头节点。
- 在方法中，首先定义了四个变量：h, length, intv, res。h是用来遍历链表的指针，length是用来记录链表的长度，intv是用来表示归并排序的间隔，res是用来存储排序后的链表的虚拟头节点。
- 使用一个while循环，遍历链表，计算出链表的长度length，并将h指向链表的头节点head。
- 使用一个while循环，根据intv的大小进行归并排序。初始时intv为1，表示每个节点都是一个有序的子链表，然后将相邻的两个子链表合并成一个更大的有序子链表，重复这个过程直到intv大于等于length，表示整个链表已经有序。
- 在每次归并排序的过程中，使用三个指针：pre, h1, h2。pre是用来指向已经排序好的部分的最后一个节点，h1和h2是用来指向待合并的两个子链表的头节点。使用两个while循环，分别找到h1和h2，并记录它们的长度c1和c2。如果h2为空，表示没有需要合并的子链表，直接跳出循环。
- 使用一个while循环，比较h1和h2的值，将较小的节点接在pre后面，并更新pre, h1, h2, c1, c2。当c1或c2为0时，表示其中一个子链表已经遍历完毕，将另一个子链表接在pre后面，并更新pre, c1, c2。最后将pre.next指向h，表示已经排序好的部分和未排序的部分连接起来。
- 将intv乘以2，表示下一轮归并排序的间隔加倍。
- 返回res.next，表示排序后的链表的头节点。
'''

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1   # 计算链表长度
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:          # h是用来遍历链表的指针
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: h, i = h.next, i - 1
                if i: break # no need to merge because the `h2` is None.
                h2, i = h, intv   # h1和h2是用来指向待合并的两个子链表的
                while i and h: h, i = h.next, i - 1
                c1, c2 = intv, intv - i # the `c2`: length of `h2` can be small than the `intv`.
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: pre.next, h1, c1 = h1, h1.next, c1 - 1 # pre是用来指向已经排序好的部分的最后一个节点
                    else: pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next
