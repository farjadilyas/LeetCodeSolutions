"""
 206. Reverse Linked List
 [ Easy ] [ 71.1% ] -- Solved 12/07/2022
 -------------------------------
 Approach:
 - Single iteration, remember next node, set current node's next to previous node

 Time Complexity: O(N)
 Space Complexity: O(N) - using input itself
"""


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev