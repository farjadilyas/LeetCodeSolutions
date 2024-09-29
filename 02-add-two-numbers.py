"""
  2. Add two numbers
  [ Medium ] | [ 38.9% ] -- Solved 24/06/2022 -- [ List ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 97.95%
  MEMORY USAGE: 83.43%

  Approach:
  Given two lists, with the numbers written in reverse order (leftmost is unit).
  In one pass, we add two lists, node by node. The l2 list is used as the answer list, if it falls
  short in size, it is linked to the remaining l1 list. Efficient on time and space
  - Adding two lists sounds easy, the slight twist is that the lists may not be the same size, one may be shorter than
    the other

  Intuition:
  - Simplify this problem by deciding that l1 is going to be the longer list. If it turns out to be the shorter one,
    we can link l1's last node to the first remaining l2 node. The remaining nodes just need the carry, if any, to be
    added to them

  Time Complexity: O(N)
  Space Complexity: O(1) -- using input as the output list
"""


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_prev = None
    head = l1
    quotient = 0
    # Add nodes and store result in l1 until one of the lists run out
    while l1 and l2:
        quotient, l1.val = divmod(l1.val + l2.val + quotient, 10)
        l1_prev = l1
        l1, l2 = l1.next, l2.next
    # If l1 runs out, we need to link l1_end to l2 since results need to be in l1 so it needs to have enough nodes
    # But if l2 runs out, nothing like this is required
    if not l1:
        l1 = l1_prev.next = l2
    # Do carry forward through the nodes of the remaining list
    while quotient and l1:
        quotient, l1.val = divmod(l1.val + quotient, 10)
        l1_prev = l1
        l1 = l1.next
    # If quotient is still remaining, add a new last node for it
    if quotient:
        l1_prev.next = ListNode(val=quotient, next=None)
    return head
