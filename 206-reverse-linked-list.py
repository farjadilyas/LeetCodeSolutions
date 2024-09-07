"""
 206. Reverse Linked List
 [ Easy ] [ 71.1% ] -- Solved 12/07/2022
 -------------------------------
 Approach:
 - Single iteration, remember next node, set current node's next to previous node
 - Move forward by setting previous=current and current=next

 Time Complexity: O(N)
 Space Complexity: O(N) - using input itself
"""


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """Iterative solution"""
    cur = head
    prev = None
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Recursive solution"""
        if not head or not head.next:
            return head
        tail = self.reverseList(head.next)
        # 3 -> 4 <- 5, when head is at 3, make 4.next=3 and 3.next=None, so: 3 <- 4 <- 5
        head.next.next = head
        head.next = None
        return tail
