class Trie:
    def __init__(self):
        self.val = 0
        self.children = dict()


class MapSum:

    def __init__(self):
        self.root = Trie()

    def insert(self, key: str, val: int) -> None:
        p = self.root
        for c in key:
            if c not in p.children:
                p.children[c] = Trie()
            p = p.children[c]
        p.val = val

    def sum(self, prefix: str) -> int:
        self.sum_ = 0
        p = self.find_prefix(prefix)
        self.traverse(p)
        return self.sum_


    def find_prefix(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p.children:
                return None
            p = p.children[c]
        return p

    def traverse(self, p):
        if not p:
            return 
        self.sum_ += p.val
        if not p.children:
            return 
        for c in p.children.keys():
            self.traverse(p.children[c])
        return 

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)