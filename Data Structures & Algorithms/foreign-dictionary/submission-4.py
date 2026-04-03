import string
from collections import defaultdict
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Create adjacency list
        dic = defaultdict(list)
        in_graph = set()

        for word in words:
            for c in word:
                in_graph.add(c)

        for i in range(1, len(words)):
            word_0 = words[i - 1]
            word_1 = words[i]
            min_len = min(len(word_0), len(word_1))
            found = False
            for c_idx in range(min_len):
                if word_0[c_idx] != word_1[c_idx]:
                    dic[word_0[c_idx]].append(word_1[c_idx])
                    found = True
                    break
            # Invalid case: prefix conflict like ["abc", "ab"]
            if not found and len(word_0) > len(word_1):
                return ""

        visited = set()
        on_path = set()
        output = []

        def dfs(c):
            if c in on_path:
                return False  # cycle
            if c in visited:
                return True
            on_path.add(c)
            for nei in dic[c]:
                if not dfs(nei):
                    return False
            on_path.remove(c)
            visited.add(c)
            output.append(c)
            return True

        for c in in_graph:
            if not dfs(c):
                return ""

        return "".join(reversed(output))