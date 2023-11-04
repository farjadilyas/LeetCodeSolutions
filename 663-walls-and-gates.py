from typing import (
    List,
)
INF = 2147483647


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        queue = []
        m, n = len(rooms), len(rooms[0])
        for r in range(m):
            for c in range(n):
                if rooms[r][c] == 0:
                    queue.append((r,c))
        while queue:
            room = queue.pop(0)
            cur_dist = rooms[room[0]][room[1]]
            if room[0] > 0 and rooms[room[0]-1][room[1]] == INF:
                rooms[room[0]-1][room[1]] = cur_dist+1
                queue.append((room[0]-1, room[1]))
            if room[0] < m-1 and rooms[room[0]+1][room[1]] == INF:
                rooms[room[0]+1][room[1]] = cur_dist+1
                queue.append((room[0]+1, room[1]))
            if room[1] > 0 and rooms[room[0]][room[1]-1] == INF:
                rooms[room[0]][room[1]-1] = cur_dist+1
                queue.append((room[0], room[1]-1))
            if room[1] < n-1 and rooms[room[0]][room[1]+1] == INF:
                rooms[room[0]][room[1]+1] = cur_dist+1
                queue.append((room[0], room[1]+1))
        return rooms
