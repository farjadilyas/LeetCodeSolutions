"""
  23. Merge k Sorted Lists
  [ Hard ] | [ 47.8% ] -- Solved 30/07/2022 -- [ Linked List, Heap ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 97.16%
  MEMORY USAGE: 42.80%

  Problem Statement:
  - You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
  - Merge all the linked-lists into one sorted linked-list and return it.

  APPROACH: Consider k nodes at a time, order using min-heap
  - At any moment, we have access to k nodes that are the current heads of k lists
  - Since we are told that each list is sorted, the most efficient way is to consider the lists from smallest to largest

  - Consider the k nodes available at any moment
  - Pick the smallest, add it to the answer linked list
  - Advance the head of the linked list which held the smallest node, and add it to the list of k nodes being considered

  OPTIMIZATION
  - The Naive way to consider and update the k nodes being considered is a O(k) scan to find the smallest, and an O(K)
    scan to update the list with a new consideration
  - This fits into the use case of a heap, which is used to keep items in order where the minimum element will be
    required and new elements need to be added efficiently
  - Hence, initialize and maintain a min-heap of size k
    - Use heappop() to get the minimum node to be added to the answer linked list
    - Use heappush() to add the new consideration obtained when the head of the linked list with the smallest node is
      advanced

  Time Complexity: O(Nlogk) - N nodes in a total of k lists
  Space Complexity: O(k)
"""


import heapq


def mergeKLists(self, lists):
    hp = []
    for i, ls in enumerate(lists):
        if ls:
            # Push (priority, list index, current head of list)
            heapq.heappush(hp, (ls.val, i, ls))
    head = cur = ListNode()
    while hp:
        popped = heapq.heappop(hp)
        cur.next = popped[2]
        cur = cur.next
        ls = lists[popped[1]] = lists[popped[1]].next
        if ls:
            heapq.heappush(hp, (ls.val, popped[1], ls))
    cur.next = None
    return head.next
