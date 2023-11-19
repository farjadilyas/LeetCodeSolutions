"""
  127. Word Ladder
  [ Medium ] | [ 39.3% ] -- Solved 04/11/2023 -- [ Graph, Union Find ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 99.35%
  MEMORY USAGE: 97.85%

  Problem:
  - Find the shortest transformation sequence that goes from beginWord to endWord
  - each adj node in the sequence can only differ by a character
  - all nodes in the sequence must be in the wordList except for beginWord, beginWord may or may not be in wordList

  Constraints:
  - 1 <= wordList.length <= 5000
  - 1 <= beginWord.length <= 10

  Approach:
  - Unweighted graph shortest path: Best algo is BFS
  - The challenge is how to construct the graph
  - Graph will contain all nodes (wordList U beginWord), an edge should be added between two nodes iff they differ
    by exactly one character

  Naive graph construction:
  - Go through all pairs of nodes, if they differ by one, add an edge
  - This is O(E^2) - worst case (for len(wordList) == 5000) -> 25,000,000

  Lazy graph construction (consider all words offset by 1 char, check if they're in wordList)
  - Step #1: Create wordSet from wordList
  - Start BFS
  - When a node is popped, for each char of the word being considered, consider letters a through z,
    thereby considering all possible words offset by one char
  - For each of those words, add them to the BFS queue if they're in wordSet
  - This set construction is O(E), and it only takes the BFS to O(beginWord.length * V)
  - Which, at worst case (word being of length 10), is: O(26*10*V) -> 260*5000
  - We can see that this approach overtakes the naive graph construction approach for wordList.length > 260
    - if wordList.length == 261 -> naive approach: 261^2, 260*261
  - So we can see this will avoid TLE for the given constraints

  Time Complexity: O(E+V)
  Space Complexity: O(V) - wordSet + wide graph
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_len = len(beginWord)
        wordSet = set(wordList)
        wordSet.add(beginWord)
        if endWord not in wordSet:
            return 0
        queue = [beginWord]
        level = 1
        while queue:
            qsize = len(queue)
            for i in range(qsize):
                node = queue.pop(0)
                if node == endWord:
                    return level
                for i in range(word_len):
                    first_half, second_half = node[:i], node[i + 1:]
                    for i in range(97, 123):
                        word = f"{first_half}{chr(i)}{second_half}"
                        if word in wordSet:
                            wordSet.remove(word)
                            queue.append(word)
            level += 1
        return 0
