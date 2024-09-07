"""
 21. Merge Two Sorted Lists
 [ Medium ] [ 61.0% ] -- Solved 12/07/2022

 Approach:
 - At every step you will be comparing two nodes and adding the smaller node to the final merged list
 - Maintain the following two pointers:
    - current: will point to the tail of the merged list (always the smaller node)
    - other: will be pointing to the tail of the other list (always the bigger node)
    - if current.next is ever smaller than other.val, current must link to other, and other must be set to current.next
    - so that current continues to be smaller and other continues to be bigger
    - eg:
        - list1: [1,2,5,6]
        - list2: [3,4,7,8]
        - after 4 iterations,current will be at 4 (merged list = 1->2->3->4) and other will be at 5
    - if current.next is None, that means that current should link up with the remaining nodes
    - other can never be None since it only changes to current.next which won't be None

 Time Complexity: O(N)
 Space Complexity: O(1)
"""


def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1: return list2
    if not list2: return list1
    current, other = (list1, list2) if list1.val < list2.val else (list2, list1)
    head = current
    while current.next:
        # if current's next value is too big, link current to other, and the big value becomes other
        if current.next.val > other.val:
            break_point = current.next
            current.next = other
            other = break_point
        current = current.next
    current.next = other
    return head
