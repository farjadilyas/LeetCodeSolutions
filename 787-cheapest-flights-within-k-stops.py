"""
  787. Cheapest Flights Within K Stops
  [ Medium ] | [ 37.4% ] -- Solved 17/12/2023
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 92.0%
  MEMORY USAGE: 53.8%

  Problem:
  - Given a network of flights, find the cheapest flight between 2 points that has at most k stops in the middle

  Approach:
  - Shortest path with a twist
  - Several different approaches are possible

  - At first glance, its clear that some sort of BFS solution is necessary since that will be able to deal with the
    k stops condition
  - My first thought was to make a subgraph that only contains paths with few hops
    - Found out this is not feasible from dry runs
    - If there are edges that leapfrog certain nodes, then edges that participate in paths that are too long will be
      included
    - So building a subgraph then applying Dijkstra's Algo won't work

  - Then I noticed that there is no need to apply something like Dijkstra's algo if we will be carrying out a BFS
  - By doing a BFS traversal we will encounter all the info we need to get the shortest path that is at most k+1 edges
    long

  - We will need a weights array to update weights of new children explored in a BFS Level
  - But notice how if we do this normally (using a single array), we can see that we inadvertently include paths
    that are too long, even if we have only run BFS on less levels
  - This can happen when we are on the final level and, for eg:
    - queue: [1,2]
    - popleft gives 1, 1 updates the weight of 2 by traversing a new edge
    - popleft then gives 2, 2 uses its lowered weight to go to 3
    - NOTE: here, we update 2 to use the max number of stops, and then update 3 to use 1 more than the max
  - REALISE that here, 2 should NOT use its updated weight

  - HENCE, we need a modification where we introduce a temp array, and for a given BFS level, we store the updated
    weights in the new array. But we don't use the updated weights until the next iteration

  COMMENTS:
  - Note that the algo we had before the modification was the Bellman-Ford shortest path algorithm
  - The final algorithm is therefore a modification of the Bellman-Ford shortest path algorithm

  Time Complexity: O(kV) - k is the max levels of BFS, E
  Space Complexity: O(E)
"""


from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append(flight)
        weights = [10_000_000 for _ in range(n)]
        weights[src] = 0
        tmp_weights = weights.copy()
        queue = deque()
        queue.append(src)
        k+=1
        while queue and k:
            for level_node in range(len(queue)):
                node = queue.popleft()
                for flight in graph[node]:
                    if weights[node] + flight[2] < tmp_weights[flight[1]]:
                        tmp_weights[flight[1]] = weights[node] + flight[2]
                        queue.append(flight[1])
            for i in range(n):
                weights[i] = tmp_weights[i]
            k -= 1
        return weights[dst] if weights[dst] < 10_000_000 else -1