class TrieNode():
    def __init__(self):
        # b : TrieNode for b
        self.children = {}
        self.eow= False


class WordDictionary:
# create a trie structure

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currptr = self.root
        for i in range(len(word)):
            if word[i] in currptr.children:
                currptr = currptr.children[word[i]]
            else:
                currptr.children[word[i]] = TrieNode()
                currptr = currptr.children[word[i]]
            
            # check for eow
            if i == len(word) - 1:
                currptr.eow = True

    def search(self, word: str) -> bool:
        
        def searchHelper(currword, currptr):
            if currword == "" :
                return currptr.eow

            if currword[0] == ".":
                for char in currptr.children.keys():
                    trialptr = currptr.children[char]
                    if searchHelper(currword[1:], trialptr):
                        return True
                return False
            else:
                #currword[0] is a char
                if currword[0] not in currptr.children:
                    return False
                return searchHelper(currword[1:], currptr.children[currword[0]])
    
        return searchHelper(word, self.root)