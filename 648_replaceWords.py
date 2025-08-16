class TrieNode:
    def __init__(self):
        self.val = None
        self.children = dict()
class TrieTree:
    def __init__(self):
        self.root = TrieNode()

    def put(self, prefix):
        root = self.root
        for c in prefix:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.val = "#"
    
    def getShortestPrefix(self, word):
        root = self.root
        prefix = []
        for i, c in enumerate(word):
            if c not in root.children:
                # return "".join(prefix)
                break
            if root.children[c].val == "#":
                # return "".join(prefix)
                return word[:i+1]
            root = root.children[c]
            # prefix.append(c)
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # dictionary_set = set(dictionary)
        dict_tree = TrieTree()
        n = len(sentence)
        words = sentence.split(" ")
        for prefix in dictionary:
            dict_tree.put(prefix)
        res = []
        for word in words:
            pref = dict_tree.getShortestPrefix(word)
            # if not pref: pref = word
            res.append(pref)
        return " ".join(res)   # 注意这里join的应该是res而不是pref，pref里边是最后一轮循环的输出


        

