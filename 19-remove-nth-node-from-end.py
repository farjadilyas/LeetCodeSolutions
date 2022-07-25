"""
 19. Remove Nth Node From End of List
 [ Medium ] [ 38.8% ] -- Solved 12/07/2022

 Approach:
 - Use two pointers, move one n steps forward
 - Then move both forward in lock-step till the one that moved first has reached the end of the list
 - Remove the node pointed to by the back pointer

 Time Complexity: O(N)
 Space Complexity: O(1)
"""


def removeNthFromEnd(self, head, n: int):
    # Move the front pointer n steps forward
    front = head
    for i in range(n):
        front = front.next

    # If front is None, then the first node needs to be removed
    if front is None:
        head = head.next
    else:
        # Move the front and back pointer till the front hits the end
        back = head
        while front.next is not None:
            front = front.next
            back = back.next

        # Back now points to the node preceding the one that needs to be removed
        back.next = back.next.next

    return head
