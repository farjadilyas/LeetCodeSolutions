"""
  211. Design Add and Search Words Data Structure
  [ Medium ] | [ 45.8% ] -- Solved 12/02/2023 -- [ DFS, Trie ]

  Problem Statement:
  - Self explanatory - search strings can also have a '.' character that matches any character

  Approach:
  - Implement a Trie - implement DFS for search - necessary due to the presence of the wildcard '.' character
"""

class Node:
    def __init__(self, val, terminal=False):
        self.hm = {}
        self.val = val
        self.terminal = terminal


class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.hm:
                n = Node(c)
                cur.hm[c] = n
                cur = n
            else:
                cur = cur.hm[c]
        cur.terminal = True

    def search(self, word: str) -> bool:
        return self._search(word, self.root, 0)

    def _search(self, word, cur, start):
        if start == len(word):
            return cur.terminal
        if word[start] != '.':
            nxt = cur.hm.get(word[start], None)
            return self._search(word, nxt, start + 1) if nxt else False

        for c, nxt in cur.hm.items():
            if self._search(word, nxt, start + 1):
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)