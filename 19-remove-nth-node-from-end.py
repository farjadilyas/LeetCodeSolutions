"""
 19. Remove Nth Node From End of List
 [ Medium ] [ 38.8% ] -- Solved 12/07/2022

 Approach:
 - Use two pointers, move one n steps forward
 - Then move both forward in lock-step till the one that moved first has reached the end of the list
 - Drop the (back pointer + 1)th node

 Time Complexity: O(N)
 Space Complexity: O(1)
"""


def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # Add a dummy head - makes the scenario where the head itself needs to be removed easier
    head = ListNode(next=head)
    # Give end_ptr an N-step head start
    end_ptr = head
    for i in range(n):
        end_ptr = end_ptr.next
    n_back_ptr = head
    # Here, checking for end_ptr.next instead of end_ptr means marker stops one node before the one to be removed
    while end_ptr.next:
        end_ptr = end_ptr.next
        n_back_ptr = n_back_ptr.next
    # drop nth node from the end
    n_back_ptr.next = n_back_ptr.next.next
    return head.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
