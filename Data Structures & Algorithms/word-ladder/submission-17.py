from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #create adjacency list
        # hotword: [list of all words that work with it]
        if endWord not in wordList:
            return 0
        dic = defaultdict(list) 

        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                hotword = word[:i] + "*" + word[i +1: ]
                dic[hotword].append(word)

        #BFS
        ret = 1
        visited =set([beginWord])

        q = deque([beginWord])
        while q:
            
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return ret
                #add the neighbors to the q
                for char in range(len(word)):
                    hotword = word[:char] + "*" + word[char +1:]
                    for neighbor in dic[hotword]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)

            ret +=1
            

        return 0