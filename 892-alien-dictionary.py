from typing import (
    List,
)
from collections import defaultdict


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words: List[str]) -> str:
        if not words: return ""
        graph = defaultdict(list)
        prev_word = words[0]
        for idx in range(1, len(words)):
            word = words[idx]
            mismatch_found = False
            for c_idx, char in enumerate(word):
                if not mismatch_found and c_idx < len(prev_word) and prev_word[c_idx] != char:
                    graph[prev_word[c_idx]].add(char)
                    mismatch_found = True
                if char not in graph:
                    graph[char] = []
            if not mismatch_found and len(prev_word) > len(word):
                return ""
            prev_word = word

        # DAG representing sorting priority is ready at this point
        # Need a topological ordering of this graph to get the letters in sorted order
        output = [None for _ in range(len(graph))]
        output_idx = len(output) - 1

        def dfs(val, out_idx):
            children = graph[val]
            # Setting children to None is a hint that this node is in the stack
            # If current node is already in the stack, this is not a DAG
            if children is None:
                return None
            graph[val] = None
            for child in children:
                if child in graph:
                    out_idx = dfs(child, out_idx)
                    if out_idx is None:
                        return None
            output[out_idx] = val
            # Way of marking node as visited
            del graph[val]
            return out_idx - 1

        sorted_keys = list(graph.keys())
        sorted_keys.sort(reverse=True)
        for val in sorted_keys:
            if val in graph:
                output_idx = dfs(val, output_idx)
                if output_idx is None:
                    return ""
        return ''.join(output)
