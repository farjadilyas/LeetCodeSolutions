"""
  2013. Detect Squares
  [ Medium ] | [ 50.4% ] -- Solved 04/11/2023 -- [ Array, Hash Table, Design, Counting ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 99.60%
  MEMORY USAGE: 70.93%

  Problem:
  - Design a data structure that consumes a stream of points on the X-Y plane, and stores them
  - Given a query point, it counts the number of ways an axis-aligned square can be formed with the query point as one
    of the vertices
  - Duplicate points are allowed and count as two separate points

  Approach:
  - Look to use hashmap(s) to reduce the lookup time to constant
  - Given a query point:
    - Do a constant lookup to find all points along the same vertical line (same x coord value)
    - Since we're looking for squares, iterate through all those vertical points..
      - Calculate the difference in the y axis values, and do another couple of constant lookups to find the other
        two points that make up the square
      - the 4 points:
        1. query point
        2. vertical point with same x coord
        3. (query[x] ± vertical_difference, query[y])
        4. (query[x] ± vertical_difference, vertical_point[y])
  - Design the hashmap(s) so that they support these operations, one approach is:
    - one hashmap to store the vertical coords for each x
    - one hashmap to store the counts of each coord for each (x,y)

  Time Complexity:
  - add: O(1)
  - count: O(N)
  Space Complexity: O(N)
"""


class DetectSquares:

    def __init__(self):
        self.vertical_index = {}
        self.coord_map = {}

    def add(self, point: List[int]) -> None:
        # add to vertical HM
        # add to coord HM
        # Time: O(1)
        # Space: O(1)
        point = (point[0], point[1])
        num_instances = self.coord_map.get(point, 0)
        self.coord_map[point] = num_instances + 1
        if not num_instances:
            if point[0] not in self.vertical_index:
                self.vertical_index[point[0]] = [point]
            else:
                self.vertical_index[point[0]].append(point)

    def count(self, point: List[int]) -> int:
        # Get all vertical points - O(1)
        # For each vertical point, do 3 coord HM lookups - O(1)
        # check for positive area
        point = (point[0], point[1])
        vertical_points = self.vertical_index.get(point[0])
        if not vertical_points:
            return 0
        res = 0
        for vertical_point in vertical_points:
            vertical_distance = point[1] - vertical_point[1]
            if not vertical_distance:
                continue
            vertical_point_count = self.coord_map.get(vertical_point, 0)
            res += vertical_point_count * self.coord_map.get((point[0] + vertical_distance, point[1]),
                                                             0) * self.coord_map.get(
                (point[0] + vertical_distance, vertical_point[1]), 0)
            res += vertical_point_count * self.coord_map.get((point[0] - vertical_distance, point[1]),
                                                             0) * self.coord_map.get(
                (point[0] - vertical_distance, vertical_point[1]), 0)
        return res
