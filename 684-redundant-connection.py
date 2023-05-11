from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Build adjacency list
        adj = defaultdict(list)
        for eid, edge in enumerate(edges):
            adj[edge[0]].append((eid, edge[1]))
            adj[edge[1]].append((eid, edge[0]))
        # visited for cycle detection, cycleStart - node that links cycle to rest of the graph - used to indicate
        # that we still need to backtrack to the start and calculate the maxEdgeId in the cycle
        visited = [False for _ in range(len(adj)+1)]
        cycleStart = None
        def dfs(node, prevEdgeId):
            global cycleStart
            nodeId = node[1]
            # If node is already visited, we found the cycle, set the cycleStart, and return -1
            # (represents an outgoing edge in the cycle)
            if visited[nodeId]:
                cycleStart = nodeId
                return -1
            visited[nodeId] = True
            for child in adj[nodeId]:
                if child[0] == prevEdgeId:
                    continue
                # None if no cycle is found, maxEdgeId in the cycle (except for this attempted step) if cycle is found
                res = dfs(child, child[0])
                if res is None:
                    continue
                # If we are back at the cycleStart, we have finalized the answer edge
                # (needs to be the one that occurs latest in the input array) - reset cycleStart
                if nodeId == cycleStart:
                    cycleStart = None
                if cycleStart is None:
                    return res
                return max(child[0], res)
            visited[nodeId] = False
            return None
        return edges[dfs((None, 1), None)]