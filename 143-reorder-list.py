"""
 143. Reorder List
 [ Medium ] [ 38.8% ] -- Solved 12/07/2022
 ---------- {{ SUBMISSION STATS: Approach 2 }} ---------------
  FASTER THAN: 82.26%
  MEMORY USAGE: 63.99%

 Problem:
 - Given a list in the Form N1 -> N2 -> ... -> Nn
 - Reorder the list in the following manner: N1 -> Nn -> N2 -> Nn-1 -> ...
"""


"""
[SUBOPTIMAL]: QUADRATIC TIME, CONSTANT SPACE

  - Let's say the current pointer is at head
  - We need to:
    - link current to last & last to current+1
    - set second_last_node.next=None (so this is the last node in next iter)
  - eg: [1 -> 2 -> 3 -> 4 -> 5 -> 6] ------------ current is at 1
    - 1st iter: 1 -> 6 -> 2 -> 3 -> 4 -> 5 ------ current is at 2
    - 2nd: iter: 1 -> 6 -> 2 -> 5 -> 3 -> 4 ----- current is at 3
  
  Edge case:
  - When the last two nodes are left, these are already correctly setup so leave them
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        current = head
        while current.next:
            second_last = middle = end = current.next
            while middle.next:
                second_last = middle
                middle = middle.next
            # if middle == end, these are the last 2 nodes and are already in the correct order
            if middle != end:
                current.next = middle
                middle.next = end
                second_last.next = None
            current = end
        return head


"""
[SUBOPTIMAL]: REVERSE HALF OF LIST USING STACK
 - Key Insight: The list is a singly linked list, but we need access to two pointers on each end of the list, both of
   which come closer to the middle. This gives us access to the nodes needed for the reordering.
   - A singly linked list does not allow us to bring the second pointer closer to the middle.. there is a need to access
     one half of the list in the reverse order of the order the singly linked list supports

 - IDEA:
   - Use fast and slow pointer to get access to middle of list
   - Save first half of list in stack
   - can access the first half in reverse order, the second half in the intended order and reorder the elements as needed
   
 - EDGE CASE:
   - Need to handle the case of the end node separately, it needs to be set to None explicitly. In other cases, the
     node preceding the pointer for the second half of the list has already been set in its new place and its next
     pointer is already set

 Time Complexity: O(N)
 Space Complexity: O(N) - Need to save half of the list in stack
"""


def reorderList(self, head) -> None:
    slow = fast = ListNode(0, head)
    stack = []
    while fast is not None and fast.next is not None:
        slow = slow.next
        stack.append(slow)
        fast = fast.next.next

    if fast:
        end = slow.next
    else:
        end = slow
    temp = end.next
    end.next = None
    slow = temp
    stack.pop()

    while stack:
        first = stack.pop()
        temp = first.next
        first.next = slow
        s_temp = slow.next
        slow.next = temp
        slow = s_temp

    return head


"""
 [OPTIMAL]: ACTUALLY REVERSE HALF OF LIST BY MANIPULATING POINTERS
 
 Use the same insights and problems from above
 
 Changes from first approach:
 - To avoid using space to enable reverse access, iterate over the second half of the list and reverse it
 - Then, iterate over the first and second half, both pointers will automatically get closer to the middle now that the
   second half of the list has been reversed. This is the access pattern we need to solve this problem.

 Time Complexity: O(N)
 Space Complexity: O(N) - Need to save half of the list in stack
"""


def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    # Use slow-fast ptrs to find the middle of the list
    slow = fast = ListNode(next=head)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Point to the second half and detach it
    shalf = slow.next
    slow.next = None

    # reverse the second half of the list
    prev = None
    current = shalf
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    # set shalf to the new head of the reversed second half
    shalf = prev
    fhalf = head

    # Now fhalf is head for the first half of the linked list
    # shalf is the head for the reversed second half of the linked list
    # eg: fhalf: 1->2->3, shalf: 6->5->4
    # desired result: 1-6-2-5-4-3, so take one from fhalf, then shalf and so on
    while fhalf and shalf:
        # Link first half to second head
        fnext = fhalf.next
        fhalf.next = shalf

        # Link second head back to first half
        snext = shalf.next
        shalf.next = fnext

        # Move the two heads forward
        fhalf = fnext
        shalf = snext
    return head


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
