class TrieNode:
    # def __init__(self, val = None, children = dict()):  # 这种初始化方式是一种陷阱：会导致每一个新建的TrieNode的children都指向同一个dict
    def __init__(self):
        self.val = None
        self.children = dict()

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            if c not in root.children: root.children[c] = TrieNode()
            root = root.children[c]
        root.val = "#"

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.children: return False
            root = root.children[c]
        if root.val == "#":
            return True
        else:
            return False


    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.children: return False
            root = root.children[c]
        return root is not None
        # return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)