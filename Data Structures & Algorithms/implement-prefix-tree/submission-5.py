class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        # self.children["a"] = TrieNode()
    

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    
    def insert(self, word: str) -> None:
        currNode = self.root

        for i, a in enumerate(word):
            if word[i] not in currNode.children:
                currNode.children[word[i]] = TrieNode()
            currNode = currNode.children[a]
            if i == len(word)- 1:
                currNode.end = True


    def search(self, word: str) -> bool:
        if word == "":
            return True
        currNode = self.root
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        if not currNode.end:
            return False
        return True

        

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
    
        return True

        
        