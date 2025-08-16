# 哈希双向链表
class ListNode:
    def __init__(self, key = 0, val = 0, next_ = None, pre = None):
        self.key = key
        self.val = val
        self.next = next_
        self.pre = pre

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.pre = self.tail, self.head
        self.cap = capacity
        self.size = 0
        self.find = dict()
    

    def move2head(self, p):  
        # p = self.find[key]
        pre = p.pre
        next_ = p.next
        pre.next = next_
        next_.pre = pre

        p.next = self.head.next
        self.head.next.pre = p
        self.head.next = p
        p.pre = self.head

    
    def del_last(self):   # 注意删除节点要在dict里边也删掉
        to_del = self.tail.pre
        pre = to_del.pre
        pre.next = self.tail
        self.tail.pre = pre
        # self.cap += 1
        self.size -= 1

        key = to_del.key
        del self.find[key]

    
    def add2head(self, p):
        next_ = self.head.next
        p.next = next_
        next_.pre = p
        self.head.next = p
        p.pre = self.head
        # self.cap -= 1
        self.size += 1

        
    def get(self, key: int) -> int:
        val = -1
        if key in self.find:
            p = self.find[key]
            val = p.val
            self.move2head(p)
        # self.print_(self.head)
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.find:
            p = self.find[key]
            p.val = value
            self.move2head(p)
        else:
            p = ListNode(key = key, val = value)
            self.find[key] = p
            # if self.cap > 0:
                # self.add2head(p)
            # else:
            if self.size >= self.cap:
                self.del_last()
            self.add2head(p)
        # self.print_(self.head)

    # def print_(self, p):
    #     while p:
    #         print(p.val, end = "")
    #         p = p.next
    #     print("---")



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)