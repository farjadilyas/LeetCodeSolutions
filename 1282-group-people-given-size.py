"""
  1282. Group the people given the group size they belong to
  [ Medium ] | [ 85.4% ] -- Solved 24/06/2022 -- [ HashMap ]

  Approach:
  Use HashMap with keys as group sizes. Values being a list of groups, a group itself is a list
  Key: List<Groups> - here, only one group is the 'active' one, the one we are inserting in, any others have been
       abandoned since they're full
  so..
  - Iterate, find the right group size list, insert in the active group, if it is full, insert an empty list for any future inputs
    - In these iterations, you already check if the active group is full. Whenever it is, add that group to the output arr
  - If the group doesn't exist in the hashmap, add it, add the list of groups for it
    - Crucially, check if the groupSize is 1, if it is, we won't get another chance to see that the group is full, so add the
      full array to the output right now and add an empty active array

  Time Complexity: O(N)
  Space Complexity: O(N) - hashmap and output list
"""


def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    hm = {}
    out = []
    for pid, groupSize in enumerate(groupSizes):
        if groupSize in hm:
            curGroup = hm[groupSize][0]
            curGroup.append(pid)
            if len(curGroup) == groupSize:
                out.append(curGroup)
                hm[groupSize].insert(0, [])
        else:
            newGroup = [pid]
            hm[groupSize] = [newGroup]
            if groupSize == 1:
                out.append(newGroup)
                hm[groupSize].insert(0, [])

    return out
