import heapq


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph, result = {}, []
        # Create adjacency list where the adj list for each node is a heap
        for ticket in tickets:
            if ticket[0] not in graph:
                graph[ticket[0]] = []
            heapq.heappush(graph[ticket[0]], (ticket[1]))

        # Pop from the heap, if a node has no more connections, add it to the result
        # This works because:
        # 1) All edges must be used
        # 2) If an edge leads to a dead end, it must occur AFTER
        # all the edges that are currently being considered, otherwise we won't be able to use all edges, contradicting
        # point 1
        def dfs(node):
            while graph.get(node):
                dfs(heapq.heappop(graph[node]))
            result.append(node)

        dfs("JFK")
        return reversed(result)
