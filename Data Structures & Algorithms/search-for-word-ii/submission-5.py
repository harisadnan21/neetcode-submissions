class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False
    def addWord(self, word):
        curr = self
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:                
                curr.children[char] = TrieNode()
                curr = curr.children[char]
        curr.eow = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        ret = set()
        # init Trie
        root = TrieNode()
        for word in words:
            root.addWord(word)
        #traverse through board
        visited = set()
        def dfs(r, c, currNode, word):
            if r< 0 or c < 0 or r > len(board) -1 or c > len(board[0]) - 1 or (r, c) in visited or board[r][c] not in currNode.children:
                return
            visited.add((r,c))
            currNode= currNode.children[board[r][c]]
            word+= board[r][c]
            if currNode.eow:
                ret.add(word)
            dfs(r + 1, c, currNode, word)
            dfs(r - 1, c, currNode, word)
            dfs(r, c + 1, currNode, word)
            dfs(r , c - 1, currNode, word)

            visited.remove((r,c))
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root, "")
                    



        return list(ret)

        