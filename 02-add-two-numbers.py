"""
  2. Add two numbers
  [ Medium ] | [ 38.9% ] -- Solved 24/06/2022 -- [ List ]
  ---------- {{ SUBMISSION STATS }} ---------------
  FASTER THAN: 97.95%
  MEMORY USAGE: 83.43%

  Approach:
  In this question, in one pass, we add two lists, node by node. The l2 list is used as the answer list, if it falls
  short in size, it is linked to the remaining l1 list. Efficient on time and space
  - Adding two lists sounds easy, the slight twist is that the lists may not be the same size, one may be shorter than
    the other

  Intuition:
  - Simplify this problem by deciding that l2 is going to be the longer list. If it turns out to be the shorter one,
    we can link l2's last node to the first remaining l1 node. The remaining nodes just need the carry, if any, to be
    added to them

  Time Complexity: O(N)
  Space Complexity: O(1) -- using input as the output list
"""


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1p = l1
    l2p = l2
    carry = val = 0
    prev = None

    # Add two numbers till one of them finishes
    while l1p is not None and l2p is not None:
        val = l2p.val + l1p.val + carry
        l2p.val = val % 10
        carry = int(val > 9)
        prev = l2p
        l1p, l2p = l1p.next, l2p.next

    # If l2 finishes, link its end to the unparsed part of l1, we can just use that part from now and add the carry, if any
    # If l2 has not finished, that means the two lists are either equal or l2 is greater, in which case, we can continue to
    # use l2 as the answer list
    if l2p is None:
        l2p = prev.next = l1p

    while carry > 0 and l2p is not None:
        val = l2p.val + carry
        l2p.val = val % 10
        carry = int(val > 9)
        prev = l2p
        l2p = l2p.next

    if carry != 0:
        prev.next = ListNode(carry)
    return l2