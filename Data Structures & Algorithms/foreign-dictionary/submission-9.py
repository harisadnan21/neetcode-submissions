import string

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # create adjacency list
        dic = {c : []  for c in string.ascii_lowercase}
        in_graph = set()
        for word in words:
            for c in word:
                in_graph.add(c)
        for idx in range(1,len(words)):
            word_0 =  words[idx -1]
            word_1 = words[idx ]
            smaller_len = min(len(word_0), len(word_1))
            c_idx = 0
            while c_idx < smaller_len and word_0[c_idx] == word_1[c_idx]:
                c_idx += 1
            
            if c_idx < smaller_len:
                dic[word_0[c_idx]].append(word_1[c_idx])
            elif len(word_0) > len(word_1):
                return ""  # Invalid: prefix longer comes first

        visited = set()
        visiting = set()
        output = []

        def dfs(char):
            if char in visited:
                return True
            if char in visiting:
                return False
            visiting.add(char)
            for elem in dic[char]:
                if not dfs(elem):
                    return False
            visiting.remove(char)
            visited.add(char)
            output.append(char)
            return True
            


        for elem in in_graph:
            if not dfs(elem):
                return ""
            
        return "".join(reversed(output))

        

        

        


        

        

        