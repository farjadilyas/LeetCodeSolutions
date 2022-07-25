"""
  2007. Find Original From Doubled Array
  [ Medium ] [ 38.4% ] -- Solved 24/06/2022
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 39.4%
  MEMORY USAGE: 36.0%

  Problem:
  An original array is transformed to a changed array by appending the double of each element in the original array
  to the original array itself. The array is then shuffled. Find the original array given the changed array.

  My Approach:
  - Intuition 1: FREQUENCY DISTRIBUTION of the distinct elements in the changed array need to be stored so that the
    double or half of the number being considered can be looked up in constant time
    - This is because one number may occur several times, so its important to make pairs, and keep track of how many
      unpaired numbers are left

  - Intuition 2: [ASCENDING ORDER] If half of the changed array has elements that are just doubles of the other half,
    we need to identify pairs between the smaller and larger number.
    - This can be done in an incorrect way, for eg, in [2,4,4,8,8,16], if you pair the 4s and 8s first, the array seems
      like an invalid array, even though it isn't and the original is [2,4,8]

    - IMPORTANT: The solution to this problem is similar to a proof by induction. If the changed array is sorted, then
      original elements will always occur before their corresponding changed (doubled) elements. This allows us to make
      pairs in the right order.Hence, when the array is sorted, then we can start to process the smallest elements first
      - Processing: taking the current element, and removing its frequency from its corresponding doubled element

    - Sample Dry Run:
      {2: 1, 4: 2, 8: 3, 16: 2}
      {2: 0, 4: 1, 8: 3, 16: 2}
      {2: 0, 4: 0, 8: 2, 16: 2}
      {2: 0, 4: 0, 8: 0, 16: 0}

  Possible Improvements (not related to approach, but implementation):
  - collections.Counter() is a great DS for Frequency Distribution. It takes in an array and results in a kind of a
    HashMap with a frequency distribution. MOREOVER, it can generate an array with the elements repeated according to
    the frequency distribution.
    - Helpful because an explicit loop isn't needed
    - Plus, an array of results doesn't need to be maintained in this case, as the frequencies are cancelled out, the
      freq dist can be changed and just converted to an array in the end.

  Time Complexity: O(N + MlogM + M) = O(N + MlogM) where M <= N
  Space Complexity: O(M)
"""


def findOriginalArray(changed):
    hm = {}
    for e in changed:
        if e in hm:
            hm[e] += 1
        else:
            hm[e] = 1

    keys = list(hm.keys())
    keys.sort()
    paired = 0
    out = []

    for key in keys:
        if key == 0:
            if hm[key] % 2 == 0:
                out.extend([key] * int(hm[key] / 2))
                paired += 1
                continue
            else:
                return []
        double_key = key * 2
        if hm[key] > 0 and double_key in hm:
            hm[double_key] -= hm[key]
            out.extend([key] * hm[key])
            hm[key] = 0
            paired += (2 if hm[double_key] == 0 else 1)

    return out if len(keys) == paired else []


"""
 Leetcode discussion solution: Same complexity as the solution above but uses collections.Counter for better time and
 memory usage since this question requires building a Frequency Distribution
"""
import collections
def findOriginalArray(changed):
    if len(changed) % 2: return []
    ctr = collections.Counter(changed)
    print(ctr)
    if ctr[0] % 2: return []
    for val in sorted(ctr):
        if ctr[val] > ctr[val * 2]: return []
        if val == 0:
            ctr[val * 2] -= ctr[val] // 2
        else:
            ctr[val * 2] -= ctr[val]
    print(ctr)
    return ctr.elements()
