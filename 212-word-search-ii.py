"""
  212. Word Search II
  [ Hard ] | [ 36.6% ] -- Solved 18/02/2023 -- [ Trie, Backtracking, Matrix ]

  Problem Statement:
  - Given an m x n board of characters and a list of strings words, return all words on the board.
  - Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
    horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
  - Note: (Not mentioned in the problem statement) - the same word should not appear twice in the results

  Broad Approach:
  - Can either iterate over words and find them on the grid, or iterate over the grid and find sequences with
    corresponding words
  - When iterating over words, for a particular word, a complete scan of the grid will be needed, with DFS being carried
    out for each cell
  - Instead of this, we can do the reverse, and iterate over the grid, using a prefix tree (Trie) to guide the DFS being
    carried out on the grid

  Approach:
  - Create a Trie of the word list
  - Iterate over the grid, for each cell, start a new DFS in 4 directions since the cells must be horizontally or
    vertically adjacent
  - Start each DFS with a reference to the root node of the Trie, each step in the DFS should correspond with a valid
    step in the Trie, if a valid step doesn't exist in the Trie, then the DFS branch can be stopped
  - Once a DFS step corresponds with a leaf node in the Trie, add the corresponding word to the result set

  Finer details:
  - The same cell cannot be used to contribute more than a single letter in a single word
      - Essentially need to make sure there isn't a cycle/intersection in the path being explored
      - Can achieve this by marking the input board's cell as traversed when its subtrees are being explored, then
        un-marking it while backtracking
  - Result set should not contain duplicate words - when a terminal node is found, just mark it non-terminal after
    adding the word to the result set

  Optimization:
  - The solution is acceptable without this optimization, however..
  - We can prune the TRIE once we know all possible outcomes for a given subtree have been explored
  - Whenever we explore a node that has no children, we can remove its connection to its parent when backtracking
  - By induction, this means that we will remove a node whenever there are no more paths to explore in the subtree
  - The Trie is kept to the minimum size needed for each step, and gives a significant improvement in the runtime
    of the solution

"""

class Node:
    def __init__(self, val, terminal=False):
        self.hm = {}
        self.val = val
        self.terminal = terminal


class WordDictionary:
    def __init__(self, words):
        self.root = Node(None)
        self.buildDictionary(words)

    def buildDictionary(self, words: List[str]):
        for word in words:
            self.addWord(word)

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.hm:
                n = Node(c)
                cur.hm[c] = n
                cur = n
            else:
                cur = cur.hm[c]
        cur.terminal = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = WordDictionary(words)
        self.board, self.m, self.n = board, len(board), len(board[0])
        self.res = []
        for i in range(self.m):
            for j in range(self.n):
                self.search(i, j, self.trie.root)
        return self.res

    def search(self, i, j, node):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.board[i][j] not in node.hm or not self.board[i][j]:
            return
        prev_node = node
        node = node.hm[self.board[i][j]]
        if node.terminal:
            self.res.append(node.terminal)
            node.terminal = False

        # Mark current cell as visited explore its subtree, then unmark it
        c = self.board[i][j]
        self.board[i][j] = None
        self.search(i - 1, j, node)
        self.search(i, j + 1, node)
        self.search(i + 1, j, node)
        self.search(i, j - 1, node)
        self.board[i][j] = c

        # Delete parent nodes if current is terminal, since all possible results for this branch of the trie have been exhausted
        if not node.hm:
            del prev_node.hm[self.board[i][j]]
