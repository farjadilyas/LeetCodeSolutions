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
APPROACH #1: REVERSE HALF OF LIST USING STACK
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
 APPROACH #2: ACTUALLY REVERSE HALF OF LIST BY MANIPULATING POINTERS
 
 Use the same insights and problems from above
 
 Changes from first approach:
 - To avoid using space to enable reverse access, iterate over the second half of the list and reverse it
 - Then, iterate over the first and second half, both pointers will automatically get closer to the middle now that the
   second half of the list has been reversed. This is the access pattern we need to solve this problem.
"""


def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """
    if head.next is None or head.next.next is None:
        return head

    middle = fast = ListNode(0, head)
    while fast is not None and fast.next is not None:
        middle = middle.next
        fast = fast.next.next
    start = head

    if fast:
        end = middle.next
    else:
        end = middle
    temp = end.next
    end.next = None
    rev = middle = temp
    nxt = rev.next

    while nxt:
        temp = nxt.next
        nxt.next = rev
        rev = nxt
        nxt = temp

    middle.next = None
    while rev:
        s_temp = start.next
        start.next = rev
        r_temp = rev.next
        start = rev.next = s_temp
        rev = r_temp

    return head
