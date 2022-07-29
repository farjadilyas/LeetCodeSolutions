"""
  25. Reverse Nodes in k-Group
  [ Hard ] | [ 52.3% ] -- Solved 30/07/2022 -- [ Linked List, Recursion ]
  ----------- {{ SUBMISSION STATS }} --------------
  FASTER THAN: 91.70%
  MEMORY USAGE: 40.10%

  Problem Statement:
  - Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list
  - Nodes that are left out as a result of not dividing cleanly, should remain as-is
  - Not allowed to change nodes, only reorder them
  - eg: 1-2-3-4-5-6-7-8-9-10-11, k=3 ---> 3-2-1-6-5-4-9-8-7-10-11

  APPROACH: Reverse Linked List Sub-problem
  - This question clearly breaks down into reverse linked list sub-problems, albeit with more edge cases and conditions

  - Reverse k nodes, remember the following pointers:
    - Head, Tail of the reversed sub-linked-list, and the next node in the normal order
    - if Tail(i) is the tail of the i-th reversed sub-linked-list, Tail(i-1).next = Head(i)

  - With this, only the edge case of a last sub-linked-list that does not divide by k...
    - For this, the most efficient way is to attempt to reverse it, if the list ends before k nodes have been reversed,
    - Reverse the already reversed sub-linked-list to obtain the original order, complying with the condition stated
      in the problem statement

  OPTIMIZATION (IMPLEMENTATION SPECIFIC)
  - It is easier to implement the code as two different functions:
    - one that reverses a sub-linked-list
    - one that uses the function above to iterate and reverse sub-linked-lists and ensure they're linked using
      Tail(i-1).next = Head(i)
  - However, if k is small relative to the size of the linked list, there are a lot of function calls
    - So unroll the function call inside the main while loop

  Time Complexity: O(N)
  Space Complexity: O(1)
"""


"""
  First Attempt: Code where every sub-linked-list is reversed with a function call (not unrolled)
  - Takes a toll on memory, 15.5MB used
"""


def reverseSubGroup(self, head, k=3):
    # 3 pointer approach for reversing linked list, prev, cur, nxt
    prev = head
    cur = head.next
    cur_k = 1

    # Iterate and reverse linked list
    while cur_k < k and cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        cur_k += 1

    # If the length of the sub-linked-list is smaller than k, then the order is meant to be left as it was
    # So, reverse the sub-linked-list we just reversed, pass in cur_k so it only attempts to reverse the number of nodes
    # we know are remaining
    if cur_k < k:
        head.next = None
        return self.reverseSubGroup(prev, cur_k)

    # start, end, next for reversed subgroup
    return prev, head, cur


def reverseKGroup(self, head, k: int):
    # Reverse the first sub-linked-list separately to obtain a pointer to the new head of the linked list
    start, prev_end, nxt = self.reverseSubGroup(head, k)
    reversed_head = start

    # Reverse the remaining sub-linked-lists
    while nxt:
        start, end, nxt = self.reverseSubGroup(nxt, k)
        prev_end.next = start
        prev_end = end

    # Ensure the new last node of the linked list terminates the linked list
    prev_end.next = None
    return reversed_head


"""
  Second Attempt: Unroll the function call for reversing a sub-linked-list inside the main while loop
  - Memory and Speed savings, 15.2MB used
"""


def reverseSubGroup(self, head, k=3):
    prev = head
    cur = head.next
    cur_k = 1
    while cur_k < k and cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        cur_k += 1

    if cur_k < k:
        head.next = None
        return self.reverseSubGroup(prev, cur_k)
    # start, end, next for reversed subgroup
    return prev, head, cur


def reverseKGroup(self, head, k):
    # Reverse the first sub-linked-list separately to obtain a pointer to the new head of the linked list
    start, prev_end, nxt_start = self.reverseSubGroup(head, k)
    reversed_head = start

    while nxt_start:
        # Same logic as that of reverseSubGroup(), but unrolled for performance
        prev = nxt_start
        cur = nxt_start.next
        cur_k = 1
        while cur_k < k and cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            cur_k += 1

        if cur_k < k:
            nxt_start.next = None
            start, end, nxt_start = self.reverseSubGroup(prev, cur_k)
        else:
            start, end, nxt_start = prev, nxt_start, cur

        prev_end.next = start
        prev_end = end

    # Ensure the new last node of the linked list terminates the linked list
    prev_end.next = None
    return reversed_head
